<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<form action="loginRegister" method ="post">
		<table
			style="background-color: skyblue; margin-left: 20px; margin-left: 20px;">
			<tr>
				<td><h3 style="color: red;">Registration Page!</h3></td>
				<td></td>
			</tr>
			<tr>
				<td>UserName :</td>
				<td><input type="text" name="username "></td>
			</tr>
			<tr>
				<td>Name :</td>
				<td><input type="text" name="name"></td>
			</tr>
			<tr>
				<td>Password :</td>
				<td><input type="password" name="password1 "></td>
			</tr>
			
			<tr>
				<td>Re-Type Password :</td>
				<td><input type="password" name="password2"></td>
			</tr>
			
			<tr>
				<td><input type="submit" name="submit" value="register"></td>
				<td> </td>
			</tr>
		</table>
	</form>
</body>
</html>