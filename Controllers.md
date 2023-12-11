In JavaServer Faces (JSF), controllers play a crucial role in managing the interaction between the user interface and the application's backend. Rather than manually creating objects of controller classes, JSF leverages the @Named annotation to automatically handle these instances.

## Contexts and Dependency Injection (CDI)

CDI is a set of services that allows Java EE components, such as EJBs and JSF managed beans, to interact in a unified way. It provides a framework for dependency injection, lifecycle management, and service lookup, enhancing modularity and making it easier to manage and integrate various components in a Java EE application.

## Creating Controller Objects in JSF

JSF does not require developers to instantiate controller classes manually. Instead, these objects are created and managed by JSF based on the defined context or scope. This approach ensures that the controller is available and properly scoped throughout its lifecycle.

## Examples and Scopes

Default Naming Example:

java
Copy code
@Named
@SessionScoped
public class WebUserController implements Serializable {
}
In this example, the object can be referred to in JSF as #{webUserController}.

## Custom Naming Example:

java
Copy code
@Named(value = "pasinduController")
@SessionScoped
public class WebUserController implements Serializable {
}
Here, the JSF refers to the object as #{pasinduController}.

JSF determines whether to create a new instance of the controller or use an existing one based on the specified scope. If an instance already exists within the required scope, JSF reuses it; otherwise, a new instance is created.

## Understanding Scopes

### ApplicationScope: This scope lasts for the duration of the application. Beans in this scope are created once and shared across all user interactions and sessions.

### SessionScope: Objects in this scope are specific to a user session. They are created at the beginning of a session and last until the session ends.

### ViewScope: In this scope, a bean remains alive as long as the user interacts with the same JSF view (page). It is useful for keeping state across postbacks in the same view.

### RequestScope: Beans in this scope are recreated with every user request. They are short-lived and disposed of once the request is processed.

### DependentScope: This is the default scope if none is specified. Beans in this scope are dependent on the lifecycle of the bean they are injected into.





