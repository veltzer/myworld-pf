# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/main/webapp/gmap.xhtml:9` - a Google Maps API key is hardcoded in the page of a public repo (already noted as a TODO in `doc/TODO.txt:8-9`). Revoke/restrict the key in the Google Cloud console and inject it at build/deploy time (e.g. a maven resource-filtered property or context-param) instead of committing it.

## Medium

- `README.md:6` - says to run with `mvn tomcat:run`, but `pom.xml:139-141` configures `tomcat7-maven-plugin`, whose goal prefix is `tomcat7`; `tomcat:` resolves to the old codehaus plugin, not the configured one. Change to `mvn tomcat7:run` (consistent with `mvn tomcat7:deploy` on line 8).
- `pom.xml:106-110` - `javax.servlet.jsp:jsp-api` is declared without `<scope>provided</scope>`, so the JSP API jar is packed into the war's WEB-INF/lib alongside the container's own copy (unlike `javax.servlet-api` on line 103). Mark it `provided`.

## Low

- `pom.xml:153` - `jetty-maven-plugin` is pinned to `9.4.0-M0`, a pre-release milestone. Move to a released 9.4.x (or drop the plugin if jetty is not used; the README only documents tomcat).
- `README.md:13-14` - documents `mvn eclipse:eclipse`; the maven-eclipse-plugin is retired and Eclipse imports maven projects directly. Remove or replace the instruction.
- `scripts/source_me.sh:6` - calls `path_abs`/`path_prefix`, which are defined nowhere in this repo, and pins long-gone local installs (JDK 1.8.0_92 line 5, maven 3.3.9 line 14, tomcat 8.0.35 line 47) plus GWT/GXT/ivy that this PrimeFaces project does not use. Delete the file or reduce it to what this repo needs.
- `src/main/webapp/index.xhtml:13-17` - the demo index links gmap, editor and dataTable but not the `pass_param_1.xhtml` parameter-passing demo, which is unreachable from the UI. Add a link.
- `doc/links.txt:2` - points to the PrimeFaces 6.0 user guide while `pom.xml:39` uses PrimeFaces 8.0; update the link to the matching version.
