const DATA_URL = 'data/data.json';
const COLUMNS = [
    {value: 'name', name: 'Название'},
    {value: 'adminDistrict', name: 'Административный округ'},
    {value: 'district', name: 'Район'},
    {value: 'address', name: 'Адрес'},
];
const COLUMNS_MAP = COLUMNS.reduce((prev, curr) => {
    return {...prev, [curr.name]: curr.value};
}, {});

const fetchJson = async (path) => {
    const response = await fetch(path);
    return await response.json();
}

const procData = (data) => {
    return data.map((item) => {
        return {
            name: `${item['Name'].slice(0, 3)} #${item['ID']}`,
            adminDistrict: item['AdmArea'],
            district: item['District'],
            address: item['Address']
        }
    })
}

const renderTable = (data, columns) => {
    const className = 'min-w-full';
    const table = document.createElement('table');
    table.setAttribute('class', className);

    const thead = createHeader(table, columns, data);
    thead.setAttribute('class', 'bg-white border-b');
    table.appendChild(thead);

    renderBody(table, data, columns);

    const root = document.getElementById('root');
    root.appendChild(table);
}

const renderBody = (table, data, columns) => {
    const tbody = createBody(columns, data);
    if (table.tBodies.length === 0) {
        table.appendChild(tbody);
    } else {
        table.replaceChild(tbody, table.tBodies[0]);
    }
    console.log('body rendered');
}

const createHeader = (table, columns, data) => {
    const className = 'text-sm font-medium text-gray-900 px-6 py-4 text-left font-bold';
    const thead = document.createElement('thead');
    const tr = document.createElement('tr');
    let th;
    for (const col of columns) {
        th = document.createElement('th');
        th.appendChild(document.createTextNode(col.name));
        th.setAttribute('class', className);
        th.addEventListener('click', (event) => {
            event.target.toggleAttribute('sorted');

            data = data.slice();
            const target = COLUMNS_MAP[event.target.innerText];
            if (event.target.getAttribute('sorted') !== null) {
                if (event.target.classList.contains('desc')) {
                    event.target.classList.replace('desc', 'asc');
                } else {
                    event.target.classList.add('asc');
                }
                data.sort((a, b) => a[target] > b[target] ? 1 : a[target] < b[target] ? -1 : 0)
            } else {
                if (event.target.classList.contains('asc')) {
                    event.target.classList.replace('asc', 'desc');
                } else {
                    event.target.classList.add('desc');
                }
                data.sort((a, b) => a[target] > b[target] ? -1 : a[target] < b[target] ? 1 : 0);
            }

            let next = event.target.nextSibling;
            while (next) {
                next.classList.remove('asc', 'desc');
                next = next.nextSibling;
            }

            let prev = event.target.previousSibling;
            while (prev) {
                prev.classList.remove('asc', 'desc');
                prev = prev.previousSibling;
            }

            renderBody(table, data, columns);
        });
        tr.appendChild(th);
    }
    thead.appendChild(tr);
    return thead;
}

const createBody = (columns, data) => {
    const className = 'text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap';
    const tbody = document.createElement('tbody');

    let tr, td;
    for (const item of data) {
        tr = document.createElement('tr');
        tr.setAttribute('class', 'bg-white border-b transition duration-300 ease-in-out hover:bg-gray-100');
        for (const col of columns) {
            td = document.createElement('td');
            td.appendChild(document.createTextNode(item[col.value]));
            td.setAttribute('class', className);
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    return tbody;
}

fetchJson(DATA_URL).then((data) => {
    data = procData(data);
    renderTable(data, COLUMNS);
})
