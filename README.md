# Crawl_News_Covid_VN


root/pom.xml

<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.6.7</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>sia</groupId>
	<artifactId>B19DCCN626_BTTH3</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>B19DCCN626_BTTH3</name>
	<description>Khong Manh Tung B19DCCN626</description>
	<properties>
		<java.version>1.8</java.version>
	</properties>
	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<optional>true</optional>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-validation</artifactId>
		</dependency>
	</dependencies>
	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
				<configuration>
					<excludes>
						<exclude>
							<groupId>org.projectlombok</groupId>
							<artifactId>lombok</artifactId>
						</exclude>
					</excludes>
				</configuration>
			</plugin>
		</plugins>
	</build>
</project>

-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/schema.sql

CREATE table if not exists Product(
    productCode VARCHAR(10) NOT NULL DEFAULT '',
    productDescription VARCHAR(100) NOT NULL DEFAULT '',
    productPrice VARCHAR(100) NOT NULL DEFAULT '0.00',
    PRIMARY KEY (productCode)
);

-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/data.sql

delete from Product;
INSERT INTO Product VALUES 
  ('8601', '86 (the band) - True Life Songs and Pictures', '14.95'),
  ('pf01', 'Paddlefoot - The first CD', '12.95'),
  ('pf02', 'Paddlefoot - The second CD', '14.95'),
  ('jr01', 'Joe Rut - Genuine Wood Grained Finish', '14.95');

-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/application.properties

spring.datasource.url=jdbc:mysql://localhost/musicdb_th3
spring.datasource.username=root
spring.datasource.password=1411
spring.datasource.initialization-mode=always
spring.jpa.hibernate.naming.physical-strategy=org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl
spring.jpa.properties.hibernate.format_sql=true
spring.datasource.driver-class-name =com.mysql.cj.jdbc.Driver

-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/templates/home.html

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Product Maintenance</title>
    </head>
    <body>
        <h1>Product Maintenance</h1>
        <a href="/displayProducts">View Products</a>
    </body>
</html>

-------------------------------------------------------------------------------------------------------------------

root/ src/main/java/web/controllers/HomeController.java

package web.controllers;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
@Controller
public class HomeController {
	@GetMapping ("/")
	public String home () {
	    return "home";
	 }
}

-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/templates/displayProducts.html

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:th="http://www.thymeleaf.org">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Product Maintenance</title>
    </head>
    <body>
        <h1>Products</h1>
            <table border="1" cellspacing="2">
                <tr>
                    <td>Code</td>
                    <td>Description</td>
                    <td>Price</td>
                </tr>
                <tr th:each="product : ${listproduct}">
                	<td th:text="${product.getProductCode()}"></td>
                	<td th:text="${product.getProductDescription()}"></td>
                	<td th:text="${product.getProductPrice()}"></td>
			        <td><a th:href="@{'/product/editProduct/' + ${product.productCode}}">EDIT</a></td>
                  	<td><a th:href="@{'/product/deleteProductPage/' + ${product.productCode}}">DELETE</a></td> 
    			</tr>
            </table>
            <a href="product/addProductPage">Add Product</a>  
    </body>
</html>

-------------------------------------------------------------------------------------------------------------------

root/ src/main/java/web/controllers/DisplayProductsController.java

package web.controllers;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMethod;
import web.models.product;
import web.repositories.productRepository;

@Controller
@RequestMapping(path = "displayProducts")
//http:localhost:8080/displayProducts
public class DisplayProductsController {
	@Autowired 															
	private productRepository ProductRepository;
	//http:localhost:8080/displayProducts
	@RequestMapping(value = "", method = RequestMethod.GET)
	public String getAllProducts(Model model) {
	    Iterable<product> listproduct = ProductRepository.findAll();
	    model.addAttribute("listproduct", listproduct);
	    return "displayProducts";
	}
}

-------------------------------------------------------------------------------------------------------------------

root/src/main/java/web/repositories/productRepository.java

package web.repositories;
import org.springframework.data.repository.CrudRepository;
import web.models.product;

public interface productRepository extends CrudRepository<product, String> {
	Iterable<product> findByProductCode(String ProductCode);
//	List<product> findByProductCode(String ProductCode);
//	product findByProductCode(String ProductCode);
}
  
-------------------------------------------------------------------------------------------------------------------

root/src/main/java/web/ models/product.java

package web.models;
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class product {
	@Id
	public String productCode;
	public String productDescription;
	public String productPrice;
	
	public product() {
		// TODO Auto-generated constructor stub
	}
	public product(String productCode, String productDescription, String productPrice) {
		this.productCode = productCode;
		this.productDescription = productDescription;
		this.productPrice = productPrice;
	}
	public String getProductCode() {
		return productCode;
	}
	public String getProductDescription() {
		return productDescription;
	}
	public String getProductPrice() {
		return productPrice;
	}
	public void setProductCode(String productCode) {
		this.productCode = productCode;
	}
	public void setProductDescription(String productDescription) {
		this.productDescription = productDescription;
	}
	public void setProductPrice(String productPrice) {
		this.productPrice = productPrice;
	}
}

-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/templates/displayUpdateProduct.html

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:th="http://www.thymeleaf.org">
    <head>
        <title>Product Maintenance</title>
    </head>
    <body>
        <h1>Update Product</h1>
            <td th:text="${messageErrorEmpty}"></td>
            <form method="POST" th:action= "@{'/product/updateProduct'}" th:object="${productFinded}">
		      
		      	  <label >Code: </label>
		      	  
			      <input disabled type="text" th:field="*{productCode}"/><br/>
			      <input type="hidden" th:field="*{productCode}"/><br/>
			      
			      <label>Description: </label>
			      <input type="text" th:field="*{productDescription}"/><br/>
			      
			      <label>Price: </label>
			      <input type="text"th:field="*{productPrice}"/><br/>
		      
		      <input type="submit" value="Update Product"/>
    		</form>
            
            <a href="../../displayProducts">
        		View Products
    		</a>
        
    </body>
</html>

-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/templates/displayAddProduct.html
  
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:th="http://www.thymeleaf.org">
    <head>
        <title>Product Maintenance</title>
    </head>
    <body>
        <h1>Add Product</h1>
          <td th:text="${messageErrorEmpty}"></td>
            <form method="POST" th:action= "@{'/product/addProduct'}" th:object="${product}"> 
		      	  <label >Code: </label>
			      <input type="text" th:field="*{productCode}"/><br/>
			      
			      <label>Description: </label>
			      <input type="text" th:field="*{productDescription}"/><br/>
			      
			      <label>Price: </label>
			      <input type="text"th:field="*{productPrice}"/><br/>
		      
		      <input type="submit" value="Add Product"/>
    		</form>
            
            <a href="../../displayProducts">
        		View Products
    		</a>
        
    </body>
</html>
  
-------------------------------------------------------------------------------------------------------------------

root/src/main/resources/templates/ displayDeleteProduct.html
  
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:th="http://www.thymeleaf.org">
    <head>
        <title>Product Maintenance</title>
    </head>
    <body>
    
    <h1><b>Are You Sure You Want To Delete This Product?</b></h1>
    
    <span>Code: </span> <span th:text="${productFinded.getProductCode()}"></span><br/>
    <span>Description: </span> <span th:text="${productFinded.getProductDescription()}"></span><br/>
    <span>Price: </span> <span th:text="${productFinded.getProductPrice()}"></span><br/>
    
    <form method="POST" th:action= "@{'/product/deleteProduct'}" th:object="${productFinded}"> 
    			  <input type="hidden" th:field="*{productCode}"/><br/>
			      <input type="hidden" th:field="*{productDescription}"/><br/>
			      <input type="hidden"th:field="*{productPrice}"/><br/>
		          <input type="submit" value="Yes"/>
    		</form>
    	
        <br/>
        <a href="../../displayProducts">
        		No
    		</a>

    </body>
</html>
  
-------------------------------------------------------------------------------------------------------------------

root/ src/main/java/web/controllers/ProductController.java

package web.controllers;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.PathVariable;
import web.models.product;
import web.repositories.productRepository;

@Controller
@RequestMapping(path = "product")
public class ProductController {
  
    @Autowired                                          
    private productRepository ProductRepository;

    //http:localhost:8080/product/editProduct/8601
    @RequestMapping(value = "/editProduct/{ProductCode}", method = RequestMethod.GET)
    public String editProduct(Model model, @PathVariable String ProductCode) {
        Optional<product> productFinded = ProductRepository.findById(ProductCode);
        model.addAttribute("productFinded", productFinded.get());
        return "displayUpdateProduct";

    }

    public static boolean isNumeric(String str) { 
          try {  
            Double.parseDouble(str);  
            return true;
          } catch(NumberFormatException e){  
            return false;  
          }  
    }
    
    @RequestMapping(value = "/updateProduct", method = RequestMethod.POST)
    public String updateProduct(Model model,
            product Product
            ) {
        
        String messageErrorEmpty = "";
        System.out.println("updateProduct");
        System.out.println(Product.getProductCode());
        System.out.println(Product.getProductDescription());
        System.out.println(Product.getProductPrice());
        
        if(Product.getProductCode().trim().isEmpty()) {
            messageErrorEmpty += "ProductCode not emty, ";
        } 
        
        if(Product.getProductDescription().trim().isEmpty()) {
            messageErrorEmpty += "ProductDescription not emty, ";
        } 
        
        if(Product.getProductPrice().trim().isEmpty()) {
            messageErrorEmpty += "ProductPrice not emty, ";
        } else {
            if(!isNumeric(Product.getProductPrice())) {
                messageErrorEmpty += "ProductPrice must be is number, ";
            } else {
                 Double tmpNum = Double.parseDouble(Product.getProductPrice());
                 if(tmpNum <= 0) {
                     messageErrorEmpty += "ProductPrice must more than 0";
                 }
            }
        }

        if(!messageErrorEmpty.equalsIgnoreCase("")) {
             product productFinded = ProductRepository.findById(Product.getProductCode()).get();
             model.addAttribute("productFinded", productFinded);
             model.addAttribute("messageErrorEmpty", messageErrorEmpty);
             return "displayUpdateProduct";
        } else {
            ProductRepository.save(Product);
            return "redirect:/displayProducts";
        }
    }
    
    @RequestMapping(value = "/addProductPage", method = RequestMethod.GET)
    public String returnPageAddProduct(Model model) {
        model.addAttribute("product", new product());
        return "displayAddProduct";
    }
    
    @RequestMapping(value = "/addProduct", method = RequestMethod.POST)
    public String addProduct(Model model,
            product Product
            ) {
        
        String messageErrorEmpty = "";
        System.out.println("addProduct");
        System.out.println(Product.getProductCode());
        System.out.println(Product.getProductDescription());
        System.out.println(Product.getProductPrice());

        if(Product.getProductCode().trim().isEmpty()) {
            messageErrorEmpty += "ProductCode not emty, ";
        } 
        
        if(Product.getProductDescription().trim().isEmpty()) {
            messageErrorEmpty += "ProductDescription not emty, ";
        } 
        
        if(Product.getProductPrice().trim().isEmpty()) {
            messageErrorEmpty += "ProductPrice not emty, ";
        } else {
            if(!isNumeric(Product.getProductPrice())) {
                messageErrorEmpty += "ProductPrice must be is number, ";
            } else {
                 Double tmpNum = Double.parseDouble(Product.getProductPrice());
                 if(tmpNum <= 0) {
                     messageErrorEmpty += "ProductPrice must more than 0";
                 }
            }
        }
        
//      if(Product.getProductPrice() <= 0) {
//          messageErrorEmpty += "ProductPrice more than 0 ";
//        }
        if(!messageErrorEmpty.equalsIgnoreCase("")) {
             model.addAttribute("messageErrorEmpty", messageErrorEmpty);
             return "displayAddProduct";
        } else {
            ProductRepository.save(Product);
            return "redirect:/displayProducts";
        }
    }
    
    @RequestMapping(value = "/deleteProductPage/{ProductCode}", method = RequestMethod.GET)
    public String returnPageDeleteProduct(Model model, @PathVariable String ProductCode) {
        Optional<product> productFinded = ProductRepository.findById(ProductCode);
        model.addAttribute("productFinded", productFinded.get());
        return "displayDeleteProduct";
    }
    
    @RequestMapping(value = "/deleteProduct", method = RequestMethod.POST)
    public String deleteProduct(Model model, product Product) {
        ProductRepository.deleteById(Product.productCode);
        return "redirect:/displayProducts";
    }
}

-------------------------------------------------------------------------------------------------------------------

root/src/main/java/web/rootApplication.java	

package web;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class rootApplication {
	public static void main(String[] args) {
		SpringApplication.run(rootApplication.class, args);}}
