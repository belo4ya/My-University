const API_URL = `https://apidata.mos.ru/v1/datasets/2985/features?api_key=484d27f7fe880f088a369b7d5cb0af55`;

const clear = (canvas) => {
    const ctx = canvas.getContext('2d');
    ctx.save();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.restore();
}

const drawPoint = (canvas, {x, y, r, color}) => {
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2, true);
    ctx.fill();
}

const drawHorizontalLine = (canvas, {begin, end, width, color}) => {
    const ctx = canvas.getContext('2d');

    ctx.strokeStyle = color;
    ctx.lineWidth = width;

    ctx.beginPath();
    ctx.moveTo(begin.x, begin.y);
    ctx.lineTo(end.x, end.y);
    ctx.stroke();
}

const fetchData = async (url) => {
    const response = await fetch(url, {
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': 'http://localhost:63342',
            'Access-Control-Allow-Credentials': 'true',
        }
    });
    const data = await response.json();

    let XYCoords = data['features'].map((item) => {
        const coordinates = item['geometry']['coordinates'];
        return {x: coordinates[0] + 180, y: coordinates[1] + 180};
    });

    const xCoords = XYCoords.map(({x}) => x);
    const yCoords = XYCoords.map(({y}) => y);

    const canvas = document.getElementById('js-canvas');
    const [width, height] = [canvas.width, canvas.height];

    const xMax = Math.max(...xCoords);
    const xMin = Math.min(...xCoords);
    const xNormalizer = (x) => {
        return function () {
            return (x - xMin) / (xMax - xMin) * width;
        }();
    };

    const yMax = Math.max(...yCoords);
    const yMin = Math.min(...yCoords);
    const yNormalizer = (y) => {
        return function () {
            return (y - yMin) / (yMax - yMin) * height;
        }();
    };

    XYCoords = XYCoords.map(({x, y}) => ({x: xNormalizer(x), y: yNormalizer(y)}));

    return data['features'].map((item, i) => {
        const attrs = item['properties']['Attributes'];
        const name = `${attrs['Name'].slice(0, 3)} ${attrs['global_id']}`;
        return {
            name: name,
            admArea: attrs['AdmArea'],
            district: attrs['District'],
            address: attrs['Address'],
            coords: XYCoords[i]
        }
    });
}

const makePointsFromData = (data, size = 3, color = 'rgb(2, 132, 199)') => {
    return data.map((item) => {
        return {...item.coords, r: size, color: color}
    });
}

const randomInt = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const generatePoints = (n) => {
    const canvas = document.getElementById('js-canvas');
    return Array.from({length: n}, () => {
        return {
            x: randomInt(0, canvas.width),
            y: randomInt(0, canvas.width),
            r: 3,
            color: 'rgb(249, 115, 22)'
        }
    });
}

const getHorizontalLine = (points, color = 'rgb(253, 224, 71, 0.5)') => {
    const sorted = points.sort(({y: aY}, {y: bY}) => aY - bY);
    const i = Math.floor(sorted.length / 2);
    let y;
    if (sorted.length % 2) {
        y = Math.round((sorted[i + 1].y - sorted[i - 1].y) / 2 + sorted[i - 1].y);
        console.log(`\nВыше: ${sorted.slice(i + 1).length}, на: 1, ниже: ${sorted.slice(0, i).length}`);
    } else {
        y = Math.round((sorted[i].y - sorted[i - 1].y) / 2 + sorted[i - 1].y);
        console.log(`\nВыше: ${sorted.slice(i).length}, на: 0, ниже: ${sorted.slice(0, i).length}`);
    }
    const canvas = document.getElementById('js-canvas');
    const lineBegin = {x: 0, y: y};
    const lineEnd = {x: canvas.width, y: y};
    return {begin: lineBegin, end: lineEnd, width: 2, color: color};
}

const showStat = (data) => {
    const adminAreaCounter = new Map();
    const districtCounter = new Map();
    for (const station of data) {
        adminAreaCounter.set(
            station.admArea,
            adminAreaCounter.get(station.admArea) === undefined ? 0 : adminAreaCounter.get(station.admArea) + 1
        );
        districtCounter.set(
            station.district,
            districtCounter.get(station.district) === undefined ? 0 : districtCounter.get(station.district) + 1
        );
    }

    console.log('Статистика по округам:');
    for (const [k, v] of adminAreaCounter.entries()) {
        console.log(`${k}: ${v} (${(v / data.length * 100).toFixed(2)}%)`);
    }

    console.log('\nСтатистика по районам:');
    for (const [k, v] of districtCounter.entries()) {
        console.log(`${k}: ${v} (${(v / data.length * 100).toFixed(2)}%)`);
    }
}

const drawCoordinates = (data) => {
    const points = [];

    const dataChecked = document.getElementById('js-checkbox-data').checked;
    if (dataChecked) {
        console.clear();
        showStat(data);
        points.push(...makePointsFromData(data));
    }

    const randomChecked = document.getElementById('js-checkbox-random').checked;
    if (randomChecked) {
        points.push(...generatePoints(80));
    }

    const canvas = document.getElementById('js-canvas');
    clear(canvas);

    if (points.length !== 0) {
        for (const point of points) {
            drawPoint(canvas, point);
        }
        drawHorizontalLine(canvas, getHorizontalLine(points));
    }
}

const main = () => {
    fetchData(API_URL).then((data) => {
        document.getElementById('js-checkbox-data').onclick = () => drawCoordinates(data);
        document.getElementById('js-checkbox-random').onclick = () => drawCoordinates(data);
        drawCoordinates(data);
    });
}

main();
