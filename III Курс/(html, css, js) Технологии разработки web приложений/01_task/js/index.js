const table = document.getElementById('main-table');
const tbody = document.createElement('tbody');
const tr = document.createElement('tr');
table.appendChild(tbody).appendChild(tr).appendChild(document.createElement('th'));

for (let i = 1; i < 11; i++) {
    const th = document.createElement('th');
    th.innerText = i.toString();
    tr.appendChild(th);
}

for (let i = 1; i < 11; i++) {
    const tr = document.createElement('tr');
    const td = document.createElement('td');
    td.innerHTML = i.toString();
    tr.appendChild(td);
    for (let j = 1; j < 11; j++) {
        const td = document.createElement('td');
        td.innerText = (i * j).toString();
        tr.appendChild(td);
    }
    tbody.appendChild(tr);
}
