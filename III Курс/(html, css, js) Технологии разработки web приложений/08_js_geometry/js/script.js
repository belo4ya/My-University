import API_KEY from "./config.js";

const API_URL = `https://apidata.mos.ru/v1/datasets/2985/features?api_key=${API_KEY}`;

const fetchData = async (url) => {
    const headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': 'http://localhost:63342',
        'Access-Control-Allow-Credentials': 'true',
    };
    const response = await fetch(url, {headers});
    let data = await response.json();
    console.log(data['features'].slice(0, 2));
    data = data['features'].map((item) => {
        return {
            name: `${item['properties']['Attributes']['Name'].slice(0, 3)} ${item['properties']['Attributes']['global_id']}`,
            adminDistrict: item['properties']['Attributes']['AdmArea'],
            district: item['properties']['Attributes']['District'],
            address: item['properties']['Attributes']['Address'],
            geometry: item['geometry'],
        }
    });
    return data;
}

fetchData(API_URL).then((data) => {
    
});
