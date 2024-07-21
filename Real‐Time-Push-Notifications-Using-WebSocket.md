## Real-Time Push Notifications in JSF/PrimeFaces Using WebSocket

### Introduction

This guide explains how to set up real-time push notifications in a JSF/PrimeFaces application using WebSocket, without relying on `p:poll`. By following these steps, you will be able to push messages from the server to the browser efficiently.

### Prerequisites

- Java EE 7 or higher
- JSF 2.2 or higher
- PrimeFaces 6.2 or higher
- A web server that supports WebSockets (e.g., Payara, TomEE)

### Step 1: Set up a WebSocket Server Endpoint

Create a WebSocket server endpoint in your JSF application.

#### 1.1 Create WebSocket Endpoint

Create a new class named `WebSocketEndpoint` in your project.

```java
import javax.websocket.OnClose;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.ServerEndpoint;
import java.io.IOException;
import java.util.concurrent.CopyOnWriteArraySet;

@ServerEndpoint("/websocket")
public class WebSocketEndpoint {

    private static final CopyOnWriteArraySet<Session> sessions = new CopyOnWriteArraySet<>();

    @OnOpen
    public void onOpen(Session session) {
        sessions.add(session);
    }

    @OnClose
    public void onClose(Session session) {
        sessions.remove(session);
    }

    @OnMessage
    public void onMessage(String message, Session session) {
        // Handle incoming messages if necessary
    }

    public static void sendMessage(String message) {
        for (Session session : sessions) {
            if (session.isOpen()) {
                try {
                    session.getBasicRemote().sendText(message);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### Step 2: Create a WebSocket Client in the Browser

Add a WebSocket client in your XHTML page using JavaScript.

#### 2.1 Modify Your XHTML Page

Edit your XHTML page to include the WebSocket client script.

```xhtml
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:h="http://xmlns.jcp.org/jsf/html"
      xmlns:p="http://primefaces.org/ui">
<h:head>
    <title>WebSocket Example</title>
    <h:outputScript>
        var websocket = new WebSocket('ws://' + window.location.host + '/yourApp/websocket');
        
        websocket.onmessage = function(event) {
            // Handle incoming messages and update the UI accordingly
            alert('Received message: ' + event.data);
            // You can also update the PrimeFaces components here
        };
        
        websocket.onclose = function() {
            console.log('WebSocket connection closed');
        };
    </h:outputScript>
</h:head>
<h:body>
    <h:form id="form">
        <!-- Your PrimeFaces components here -->
    </h:form>
</h:body>
</html>
```

### Step 3: Send Messages from the Server

Send messages to the WebSocket client from your server-side code.

#### 3.1 Create a Managed Bean

Create a managed bean to handle message sending.

```java
import javax.enterprise.context.ApplicationScoped;
import javax.inject.Named;

@Named
@ApplicationScoped
public class MessageBean {

    public void sendMessageToClient(String message) {
        WebSocketEndpoint.sendMessage(message);
    }
}
```

#### 3.2 Use the Managed Bean

Invoke the `sendMessageToClient` method from your business logic whenever you want to push a message to the client.

```java
import javax.inject.Inject;

public class SomeService {

    @Inject
    private MessageBean messageBean;

    public void someBusinessMethod() {
        // Your business logic here
        messageBean.sendMessageToClient("Hello, this is a push notification!");
    }
}
```

### Conclusion

By following these steps, you have set up real-time push notifications in your JSF/PrimeFaces application using WebSocket. This approach provides a more efficient way to push messages from the server to the client compared to using `p:poll`.


[Back](https://github.com/hmislk/hmis/wiki/Knowledge-Base)