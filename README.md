The above represents a simplified form of our a production application and it can give you an idea of what the app looks like in production.

The goal is to create a flask application that implements a very simple todo list. It would have an HTML form that accepts a new todo and displays a list of todos. The todos are persisted in the `postgres-main` database and replicated to `postgres-replica`. If you prefer Django or some other web framework that is fine too - don't focus too much on the web app/framework - python is preferred, however.

To deploy it you will the spitzkop account on GKE: Free Trial and Free Tier  |  Google Cloud  and create and deploy your application so I can connect to the deployed cluster/project.

What I expect to see as a result:

A directory under our DevOps/SRE git repo that contains the deployment scripts/manifests/etc.. that I can use to play around with the deployed cluster. If you prefer you can create a new fresh repo under spitzkop organisation

A readme file with some basic details about the app and how to test it locally and to deploy it.

Helm charts, Kustomize, Terraform or other tools are your choice - an explanation about the choice of tools would be nice to see, however.

For postgres, you can use the official docker image. Please make sure that streaming replication works with pg-replica.

Multiple options can be selected.
