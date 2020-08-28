# Dragon 🐉🔥
A service that handles todos... like a dragon?

## Local Development
To run locally simply run `docker-compose up`. This will require docker to be installed and running locally. See the tools.sh script for other project management functions. Run the script through `make`.

## Deployment
Run `make` deploy


## Project Structure
There are thousands of differnt ways to organize a project. This is how I organized this one. A lot of engineers would do it differently. You can do it differently, thats ok. As long as you have _some_ organization and can articulate why you choose it your probably doing very well.

```
|-- cloudformation
|-- site
|-- test
|-- util
\-- dragon
      |-- api.py
      |-- endpoints
      |     |-- attach.py
      |     |-- create.py
      |     |-- detatch.py
      |     |-- find.py
      |     |-- list_all.py
      |     |-- ping.py
      |     |-- remove.py
      |     \-- update.py
      |-- aws
      |     |-- client.py
      |     \-- services
      |           |-- dynamo.py
      |           |-- s3.py
      |           \-- ssm.py
      |-- model
      |     \-- todo.py
      |-- flask_dragon
      |     \-- api.py
      \-- common
            |-- codes.py
            |-- config.py
            |-- constants.py
            |-- exceptions.py
            |-- standard.py
            |-- types.py
            \-- middleware
                  |-- authorize.py
                  |-- catch_errors.py
                  \-- cors.py
```

## /dragon
- all your code should be organized under this directory
- you can name it nearly anything you want (`src`, `api_server`, `server`, `api`, or something specific to your application [`dragon`]). Consider that the name should be specific and unique so it doesn't conflict with another library you install later.

## /endpoints
- your most high level functions/classes that handle api endpoint invocations go here
- this is a folder you should have but it could be shapped and named differently based on the framework, tooling, and architecture. For example, the `flask_restx` library uses classes called resources so when using that library this dir is typically called `resources`. This project is an api, but for applications that serve web content in flask this is commonly called `views`. The idea is always the same, when flask (or other http framework) handles an invocation to the web server the code in this directory is the first to be called.

## /aws
- this is project specific, it may not exist in your project
- In APIs this is a pretty common directory as nearlly all modern APIs are going to rely heavily on some cloud provider
- Even if this doesn't exist in your project the take away is valid: take logically related segments of your project and organize it into modules and submodules

## /model
- another very common module in APIs and apps. It often contains different content. The term `model` can apply to a database model, a data model, a class that contains the logic to manage an entity. Often times there might be two or three different modules named `model`.
- in this project, this model refers to the database
- the only model here is a `todo`. It contains a `schema` defining the shape of the database and the most fundamental methods for operating on that data.
- note, models of this type don't contain business logic
- engineers have preferred ways of structuring projects, frameworks, libraries, and languages all have standards for project structure and organization. It all changes over time. This project is about 2 years old and for me personally, its very out of date. The structure and organization is all still valid but if I made a new project it would look a lot different. Now, I would place this code somewhere like `dragon.database.model` just to be sure its clear the kind of model it is.

## /flask_dragon
- this is very project specific.. you can kind of just ignore it. I needed a specialized flask class for this api.
- same take away as always... some code is logically related? module it!

## /common
- this is very very common. It takes many names: `core`, `shared`, `base` -- pretty much anything generic
- the idea is that, you have a lot of modules that are very specific to their part of the app but here you have logic that is unspecific - it has use everywhere.
- you can put pretty much anything here but you can almost gaurntee to find something resembling a `config`, `constants`, `errors`, or `middleware` modules. They might have different names but the general idea will be the same. These are fundamental modules pretty much all apps and APIs will need.



