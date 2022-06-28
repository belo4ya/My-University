import {intersection, union} from "./sets.js";
import {drawPoint} from "./draw.js";

const API_KEY = '484d27f7fe880f088a369b7d5cb0af55';

const API_URL = `https://apidata.mos.ru/v1/datasets/2985/features?api_key=${API_KEY}`;

const COLORS = {
    RED_800: 'rgb(153, 27, 27)',
    RED_500: 'rgb(239, 68, 68)',
    RED_300: 'rgb(252, 165, 165)',
    ORANGE_800: 'rgb(154, 52, 18)',
    ORANGE_500: 'rgb(249, 115, 22)',
    ORANGE_300: 'rgb(253, 186, 116)',
    YELLOW_800: 'rgb(133, 77, 14)',
    YELLOW_500: 'rgb(234, 179, 8)',
    YELLOW_300: 'rgb(253, 224, 71)',
    LIME_800: 'rgb(63, 98, 18)',
    LIME_500: 'rgb(132, 204, 22)',
    LIME_300: 'rgb(190, 242, 100)',
}

class ChargingStation {
    name;
    adminDistrict;
    district;
    address;
    coords;

    constructor(name, adminDistrict, district, address, coords) {
        this.name = name;
        this.adminDistrict = adminDistrict;
        this.district = district;
        this.address = address;
        this.coords = coords;
    }
}

class Manager {
    #collection;
    #adminDistrictList;
    #districtList;

    constructor(collection) {
        this.#collection = collection;

        this.#adminDistrictList = new Set();
        this.#districtList = new Set();
        for (const station of collection) {
            this.#adminDistrictList.add(station.adminDistrict);
            this.#districtList.add(station.district);
        }

        this.#adminDistrictList = [...this.#adminDistrictList];
        this.#districtList = [...this.#districtList];
    }

    static async fromApi(url) {
        const response = await fetch(url, {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Access-Control-Allow-Origin': 'http://localhost:63342',
                'Access-Control-Allow-Credentials': 'true',
            }
        });
        const data = await response.json();

        const coords = data['features'].map((item) => {
            const coordinates = item['geometry']['coordinates'];
            return {x: coordinates[0] + 180, y: coordinates[1] + 180};
        });

        const xCoords = coords.map(({x}) => x);
        const yCoords = coords.map(({y}) => y);

        const xMax = Math.max(...xCoords);
        const xMin = Math.min(...xCoords);
        const xNormalizer = (x) => {
            return function () {
                return (x - xMin) / (xMax - xMin);
            }();
        };

        const yMax = Math.max(...yCoords);
        const yMin = Math.min(...yCoords);
        const yNormalizer = (y) => {
            return function () {
                return (y - yMin) / (yMax - yMin);
            }();
        };

        const collection = data['features'].map((item) => {
            const attrs = item['properties']['Attributes'];

            const name = `${attrs['Name'].slice(0, 3)} ${attrs['global_id']}`;

            let coords = item['geometry']['coordinates'];
            coords = {x: xNormalizer(coords[0] + 180), y: yNormalizer(coords[1] + 180)}

            return new ChargingStation(
                name,
                attrs['AdmArea'],
                attrs['District'],
                attrs['Address'],
                coords
            );
        });

        return new this(collection);
    }

    get adminDistrictList() {
        return this.#adminDistrictList;
    }

    get districtList() {
        return this.#districtList;
    }

    all() {
        return this.#collection;
    }

    filterBy(...by) {
        if (by.length > 0) {
            let _by = by[0];
            let prevKey = Object.keys(_by)[0];
            let init = new Set(this.#filterBy(_by));
            for (let i = 1; i < by.length; i++) {
                _by = by[i];
                const currKey = Object.keys(_by)[0]
                if (currKey === prevKey) {
                    init = union(init, new Set(this.#filterBy(_by)));
                } else {
                    init = intersection(init, new Set(this.#filterBy(_by)));
                }
                prevKey = currKey;
            }
            return [...init];
        }
        return this.#collection;
    }

    #filterBy(by) {
        const [key, value] = Object.entries(by)[0];
        return this.#collection.filter((station) => station[key] === value);
    }
}

const drawCoordinates = (manager) => {
    const root = document.getElementById('js-root');

    const div = document.createElement('div');
    div.setAttribute('class', 'flex flex-row p-5 pl-10');
    root.prepend(div);

    const adminDistrictUl = document.createElement('ul');
    for (const adminDistrict of manager.adminDistrictList) {
        const li = document.createElement('li');
        li.setAttribute('class', 'list-disc');
        li.appendChild(document.createTextNode(adminDistrict));
        adminDistrictUl.appendChild(li);
    }
    adminDistrictUl.setAttribute('class', 'mr-10');
    div.appendChild(adminDistrictUl);

    const districtUl = document.createElement('ul');
    for (const district of manager.districtList) {
        const li = document.createElement('li');
        li.setAttribute('class', 'list-disc');
        li.appendChild(document.createTextNode(district));
        districtUl.appendChild(li);
    }
    div.appendChild(districtUl);

    const canvas = document.getElementById('js-canvas');
    for (const station of manager.all()) {
        drawPoint(canvas, {...station.coords, r: 3, color: COLORS.RED_300});
    }
}

const main = () => {
    Manager.fromApi(API_URL).then((manager) => {
        drawCoordinates(manager);
    });
}

main();
