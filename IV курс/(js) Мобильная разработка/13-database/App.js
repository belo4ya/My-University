import React, {useEffect, useState} from 'react';
import {FlatList, StyleSheet, Text, TextInput, TouchableOpacity, View} from 'react-native';
import {AntDesign, MaterialIcons} from "@expo/vector-icons";
import Checkbox from 'expo-checkbox';
import * as SQLite from 'expo-sqlite';

const db = SQLite.openDatabase('todo.db');

const App = () => {
    const [todo, setTodo] = useState('');
    const [todos, setTodos] = useState([]);
    const [completedTodos, setCompletedTodos] = useState(new Set());

    useEffect(() => {
        db.transaction(tx => {
            tx.executeSql(
                'create table if not exists todo (id integer primary key not null, todo text);'
            );
        });
        updateList();
    }, []);

    const addTodo = () => {
        db.transaction(
            tx => {
                tx.executeSql('insert into todo (todo) values (?)', [todo]);
            },
            null,
            updateList
        );
    };

    const deleteTodo = id => {
        db.transaction(
            tx => {
                tx.executeSql(`delete
                               from todo
                               where id = ?;`, [id]);
            },
            null,
            updateList
        );
    };

    const markTodoCompleted = (id) => {
        const _todos = new Set(completedTodos)
        !completedTodos.has(id) ? _todos.add(id) : _todos.delete(id)
        setCompletedTodos(_todos);
    };

    const updateList = () => {
        db.transaction(tx => {
            tx.executeSql('select * from todo', [], (_, {rows}) =>
                setTodos(rows._array)
            );
        });
    };


    return (
        <View style={styles.container}>
            <TextInput
                cursorColor="#9046fd"
                style={styles.input}
                onChangeText={text => setTodo(text)}
                value={todo}
            />
            <TouchableOpacity style={styles.button} onPress={addTodo}>
                <Text style={styles.buttonText}>Add Todo</Text>
            </TouchableOpacity>
            <FlatList
                style={styles.list}
                keyExtractor={item => item.id.toString()}
                renderItem={({item}) => (
                    <View style={styles.listItem}>
                        <Checkbox
                            color="#9046fd"
                            value={completedTodos.has(item.id)}
                            onValueChange={() => markTodoCompleted(item.id)}
                        />
                        <Text
                            style={completedTodos.has(item.id) ? styles.completedTodoText : styles.todoText}>{item.todo}</Text>
                        <TouchableOpacity onPress={() => deleteTodo(item.id)}>
                            <MaterialIcons
                                name="delete"
                                size={25}
                                color={completedTodos.has(item.id) ? "#9046fd" : "#000"}
                            />
                        </TouchableOpacity>
                    </View>
                )}
                data={todos}
            />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        paddingHorizontal: 20,
        paddingTop: 50,
    },
    input: {
        borderWidth: 1,
        borderColor: '#9046fd',
        padding: 10,
        fontSize: 18,
        borderRadius: 6,
    },
    button: {
        backgroundColor: '#9046fd',
        padding: 10,
        margin: 10,
        alignItems: 'center',
        borderRadius: 6,
    },
    buttonText: {
        color: '#fff',
        fontSize: 18,
    },
    list: {
        marginTop: 20,
    },
    listItem: {
        borderColor: '#ccc',
        borderWidth: 1,
        padding: 10,
        marginBottom: 10,
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    deleteButton: {
        color: '#9046fd',
        fontSize: 18,
    },
    todoText: {
        fontSize: 18,
        fontWeight: '500'
    },
    completedTodoText: {
        fontSize: 18,
        color: '#9046fd',
        fontWeight: '400',
        textDecorationLine: 'line-through',
    },
});

export default App;