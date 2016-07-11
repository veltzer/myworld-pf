.PHONY: all
all:
	@mvn package
	@mvn tomcat7:undeploy
	@mvn tomcat7:deploy
	@gnome-open https://localhost:8443/myworld-pf

.PHONY: package
package:
	@mvn package
