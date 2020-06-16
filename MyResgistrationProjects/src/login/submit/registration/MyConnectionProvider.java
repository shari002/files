package login.submit.registration;

import java.sql.*;
import java.sql.DriverManager;


public class MyConnectionProvider implements MyProvider {
	static Connection con=null;
	public static Connection getCon() {
		try {
			Class.forName("com.mysql.jdbc.Driver"); //org.postgresql.Driver
			con = DriverManager.getConnection(connURL,username,pwd);
		} catch(Exception e) {
			System.out.println(e);
		}
		return con;
	}
}
