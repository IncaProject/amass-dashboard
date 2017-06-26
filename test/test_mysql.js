/**
 * Created by anurag on 6/23/17.
 */

var mysql = require('mysql2');

// ssh -f aaiyer@lima-vc-4.sdsc.optiputer.net -L 3307:lima.sdsc.optiputer.net:3306 -N
var db_server = "localhost";
var db_port = "3307";
var db_uid = "rehs2017";
var db_pwd = "zcWLZ9TsYP6m67";
var db_name= "amass_refactor";


// create the connection to database
const connection = mysql.createConnection({
    host: db_server,
    port: db_port,
    user: db_uid,
    password: db_pwd,
    database: db_name
});



// query and pull data from db

connection.query('select * from `amass_gateway_cipres` where `TOOL_NAME`  = ? AND `USER_SUBMIT_DATE` > ?', ['BEAST2_XSEDE', '2016-05-28'],
    function(
        err,
        rows,
        fields
    ) {
        console.log(err, rows, fields);
    });
