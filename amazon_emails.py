#!/usr/bin/python
import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = 'srinath.kodali@outlook.com'
toaddrs  = 'kodalizzzzz434@gmail.com'
msg = """From: ksrinathchowdary9@gmail.com
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test
<table class="head-wrap" bgcolor="#999999">
	<tr>
		<td></td>
		<td class="header container">
			
				<div class="content">
					<table bgcolor="#999999">
					<tr>
						<td><img src="http://placehold.it/200x50/" /></td>
						<td align="right"><h6 class="collapse">Hero</h6></td>
					</tr>
				</table>
				</div>
				
		</td>
		<td></td>
	</tr>
</table><!-- /HEADER -->
<!-- BODY -->
<table class="body-wrap">
	<tr>
		<td></td>
		<td class="container" bgcolor="#FFFFFF">

			<div class="content">
			<table>
				<tr>
					<td>
						
						<h3>Welcome, Elijah Baily</h3>
						<p class="lead">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et.</p>
						
						<!-- A Real Hero (and a real human being) -->
						<p><img src="http://placehold.it/600x300" /></p><!-- /hero -->
						
						<!-- Callout Panel -->
						<p class="callout">
							Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt. <a href="#">Do it Now! &raquo;</a>
						</p><!-- /Callout Panel -->
						
						<h3>Title Ipsum <small>This is a note.</small></h3>
						<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
						<a class="btn">Click Me!</a>
												
						<br/>
						<br/>							
												
						<!-- social & contact -->
						<table class="social" width="100%">
							<tr>
								<td>
									
									<!--- column 1 -->
									<table align="left" class="column">
										<tr>
											<td>				
												
												<h5 class="">Connect with Us:</h5>
												<p class=""><a href="#" class="soc-btn fb">Facebook</a> <a href="#" class="soc-btn tw">Twitter</a> <a href="#" class="soc-btn gp">Google+</a></p>
						
												
											</td>
										</tr>
									</table><!-- /column 1 -->	
									
									<!--- column 2 -->
									<table align="left" class="column">
										<tr>
											<td>				
																			
												<h5 class="">Contact Info:</h5>												
												<p>Phone: <strong>408.341.0600</strong><br/>
                Email: <strong><a href="emailto:hseldon@trantor.com">hseldon@trantor.com</a></strong></p>
                
											</td>
										</tr>
									</table><!-- /column 2 -->
									
									<span class="clear"></span>	
									
								</td>
							</tr>
						</table><!-- /social & contact -->
					
					
					</td>
				</tr>
			</table>
			</div>
									
		</td>
		<td></td>
	</tr>
</table><!-- /BODY -->

<!-- FOOTER -->
<table class="footer-wrap">
	<tr>
		<td></td>
		<td class="container">
			
				<!-- content -->
				<div class="content">
				<table>
				<tr>
					<td align="center">
						<p>
							<a href="#">Terms</a> |
							<a href="#">Privacy</a> |
							<a href="#"><unsubscribe>Unsubscribe</unsubscribe></a>
						</p>
					</td>
				</tr>
			</table>
				</div><!-- /content -->
				
		</td>
		<td></td>
	</tr>
</table><!-- /FOOTER -->
"""

print "Message length is " + repr(len(msg))

#Change according to your settings
smtp_server = 'get_server'
smtp_username = 'get username'
smtp_password = 'set password'
smtp_port = '587'
smtp_do_tls = True

server = smtplib.SMTP(
    host = smtp_server,
    port = smtp_port,
    timeout = 10
)
server.set_debuglevel(10)
server.starttls()
server.ehlo()
server.login(smtp_username, smtp_password)
server.sendmail(fromaddr, toaddrs, msg)
print server.quit()
