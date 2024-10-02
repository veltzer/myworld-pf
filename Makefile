##############
# parameters #
##############
# do you want to show the commands executed ?
DO_MKDBG:=0
# do you want dependency on the Makefile itself ?
DO_ALLDEP:=1

#########
# rules #
#########
.PHONY: all
all:
	@true

.PHONY: deploy
deploy:
	@mvn package
	@mvn tomcat7:undeploy
	@mvn tomcat7:deploy
	@gnome-open https://localhost:8443/myworld-pf

.PHONY: package
package:
	@mvn package

.PHONY: jetty
jetty:
	@mvn jetty:run

##########
# alldep #
##########
ifeq ($(DO_ALLDEP),1)
.EXTRA_PREREQS+=$(foreach mk, ${MAKEFILE_LIST},$(abspath ${mk}))
endif # DO_ALLDEP
