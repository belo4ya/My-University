import update from 'immutability-helper';


export function getAll() {
    return [
        {
            id: 1,
            text: '4.8 Формы',
            completed: false
        },
        {
            id: 2,
            text: '4.12 Фильтр для магазина',
            completed: false
        },
        {
            id: 3,
            text: '4.13 Список дел',
            completed: false
        },
        {
            id: 4,
            text: '4.14 Условный рендер',
            completed: false
        },
        {
            id: 5,
            text: '4.15 Компоненты основанные на классах',
            completed: false
        }
    ]
}

export function updateStatus(items, itemId, completed) {
    let index = items.findIndex(item => item.id === itemId);

    return update(items, {
        [index]: {
            completed: {$set: completed}
        }
    });
}

let todoCounter = 1;

function getNextId() {
    return getAll().length + todoCounter++;
}

export function addToList(list, data) {
    let item = Object.assign({
        id: getNextId()
    }, data);

    return list.concat([item]);
}
