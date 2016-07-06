# myworld-pf
Myworld implemented in prime faces

to compile: mvn compile

to package: mvn package

to run: mvn tomcat:run

to deploy: mvn tomcat7:deploy
	- remember to run ~/install/apache-tomcat-XXX beforehand
	- deploy does not build, remember to build before.
	- deploy does not undeploy, remember to undeploy before.

create eclipse project:
	mvn eclipse:eclipse
