package com.java.StringBuilder;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EventManager {
    Map<EventType, List<EventListener>> listeners = new HashMap<>();

    public EventManager(EventType... operations) {
        for (EventType operation: operations) {
            this.listeners.put(operation, new ArrayList<>());
        }
    }

    public void subscribe(EventType eventType, EventListener listener) {
        List<EventListener> users = listeners.get(eventType);
        users.add(listener);
    }

    public void unsubscribe(EventType eventType, EventListener listener) {
        List<EventListener> users = listeners.get(eventType);
        users.remove(listener);
    }

    public void notify(EventType eventType, String newString) {
        List<EventListener> users = listeners.get(eventType);
        for (EventListener listener : users) {
            listener.update(eventType, newString);
        }
    }

}
