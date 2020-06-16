package login.submit.registration;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/loginRegister") 
public class LoginRegister extends HttpServlet {
	private static final long serialVersionUID = 1L;
    
    public LoginRegister() {
        
    }
    
    
    

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		CustomerDAO cd = new CustomerDAOImpl();
		String userName = request.getParameter("username");
		String password = request.getParameter("password1");
		String submitType = request.getParameter("submit");
		Customer c = cd.getCustomer(userName, password);
		
		if (submitType.equals("login") && c != null && c.getName() != null) {
			request.setAttribute("message", c.getName());
			request.getRequestDispatcher("welcome.jsp");
			
			
		}else if (submitType.equals("register")) {
			c.setName(request.getParameter("name"));
			c.setPassword(password);
			c.setUsername(userName);
			cd.insertCustomer(c);
			request.setAttribute("successMessage", "Get Hype!! Now Login to Continue.");
			request.getRequestDispatcher("login.jsp").forward(request, response);
			
		}else {
			request.setAttribute("message", "Data Not Found, Click on Register! ");
			request.getRequestDispatcher("login.jsp").forward(request, response);
		}

		
		
		
		
		
	}

}
