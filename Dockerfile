FROM container-registry.oracle.com/middleware/weblogic:12.2.1.2
COPY medrec.ear physician.ear $DOMAIN_HOME/autodeploy/
COPY medrec.py /u01/oracle/
COPY seed /u01/oracle/seed
RUN sed -i -e "66r /u01/oracle/medrec.py" /u01/oracle/create-wls-domain.py
