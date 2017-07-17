readDomain(os.environ.get("DOMAIN_HOME"))

medrec_ds_name="MedRecGlobalDataSourceXA"

create(medrec_ds_name, 'JDBCSystemResource')
cd('/JDBCSystemResource/'+medrec_ds_name)
set('Target','AdminServer')
 
cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name)
cmo.setName(medrec_ds_name)

cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name)
create(medrec_ds_name,'JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
set('JNDIName', java.lang.String('jdbc/'+medrec_ds_name))
set('GlobalTransactionsProtocol', java.lang.String('TwoPhaseCommit'))

cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name)
create(medrec_ds_name,'JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName','org.apache.derby.jdbc.ClientXADataSource')
set('URL','jdbc:derby://localhost:1527/medrec;ServerName=localhost;databaseName=medrec;create=true')
set('PasswordEncrypted', 'medrec')
set('UseXADataSourceInterface', 'false')
 
cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name+'/JDBCDriverParams/NO_NAME_0')
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('user','Property')
cd('Property')
cd('user')
set('Value', 'medrec')

cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name+'/JDBCDriverParams/NO_NAME_0')
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('portNumber','Property')
cd('Property')
cd('portNumber')
set('Value', '1527')

cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name+'/JDBCDriverParams/NO_NAME_0')
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('databaseName','Property')
cd('Property')
cd('databaseName')
set('Value', 'medrec;create=true')

cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name+'/JDBCDriverParams/NO_NAME_0')
create('myProperties','Properties')
cd('Properties/NO_NAME_0')
create('serverName','Property')
cd('Property')
cd('serverName')
set('Value', 'localhost')

cd('/JDBCSystemResource/'+medrec_ds_name+'/JdbcResource/'+medrec_ds_name)
create(medrec_ds_name,'JDBCConnectionPoolParams')
cd('JDBCConnectionPoolParams/NO_NAME_0')
set('TestTableName','SQL SELECT 1 FROM SYS.SYSTABLES\r\n\r\n')

updateDomain()
closeDomain()

