# Getting the MedRec Sample Application files

1. Install WebLogic. Be sure to select the option to include the samples.
2. Copy `medrec.ear`, `physician.ear` to this directory
```
cp $ORACLE_HOME/wlserver/samples/server/medrec/dist/standalone/medrec.ear .
cp $ORACLE_HOME/wlserver/samples/server/medrec/dist/standalone/physician.ear .
```
3. Copy `medrec-data-import.jar` and `medrec-domain.jar` to the seed directory. We will need to use these when we seed the data for the MedRec application
```
cp $ORACLE_HOME/wlserver/samples/server/medrec/dist/modules/medrec-data-import.jar seed/.
cp $ORACLE_HOME/wlserver/samples/server/medrec/dist/modules/medrec-domain.jar seed/.
```

# Building this sample

```
docker build -t medrec-monolith .
```

# Running this sample

```
docker run -d -p 7001:7001 --name medrec medrec-monolith 
```

# Seeding the data

```
docker exec -ti medrec /bin/bash -c "java -classpath \$ORACLE_HOME/seed/medrec-data-import.jar:\$ORACLE_HOME/seed/medrec-domain.jar:\$ORACLE_HOME/wlserver/common/derby/lib/derbyclient.jar:\$ORACLE_HOME/wlserver/server/lib/weblogic.jar com.oracle.medrec.util.DataImporter"
```

# Accessing our application

We can access our application at `http://localhost:7001/medrec`

