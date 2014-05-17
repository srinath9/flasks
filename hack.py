from flask import Flask,render_template
app = Flask(__name__) 
import u_emails

@app.route('/options')
def options():
    user = { 'nickauthor': 'Miguel' } # fake user
    posts = [ # fake array of posts
        { 
            'author': { 'nickauthor': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickauthor': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        },
        { 
            'author': { 'nickauthor': 'Authentication' }, 
            'body': 'Failure to properly authenticate users.' 
        },
        { 
            'author': { 'nickauthor': 'Command Injection' }, 
            'body': 'Allowing user-controlled input to be injected into command lines that are created to invoke other programs, using system() or similar functions.' 
        },
        { 
            'author': { 'nickauthor': 'Cross-Site Request Forgery (CSRF)' }, 
            'body': 'Failure to verify that the sender of a web request actually intended to do so.' 
        },
        { 
            'author': { 'nickauthor': 'Cross-Site Scripting XSS' }, 
            'body': 'Failure of a site to validate, filter, or encode user input before returning it to another users web client.' 
        },
        { 
            'author': { 'nickauthor': 'Cryptographic Issue' }, 
            'body': 'An insecure algorithm or the inappropriate use of one; an incorrect implementation of an algorithm that reduces security; the lack of encryption; also, weak key or certificate management, key disclosure, random number generator problems.' 
        },
        { 
            'author': { 'nickauthor': 'Denial of Service' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickauthor': 'Design Issue' }, 
            'body': 'A vulnerability is characterized as a "Design Issue" if there exists no errors in the implementation or configuration of a system, but the initial design causes a vulnerability to exist.' 
        },
        { 
            'author': { 'nickauthor': 'Information Disclosure' }, 
            'body': 'Exposure of system information, sensitive or private information, fingerprinting, etc.' 
        },
        { 
            'author': { 'nickauthor': 'Memory Corruption' }, 
            'body': 'Any form of Memory Corruption: Buffer Overflow, Use After Free, etc.' 
        },
        { 
            'author': { 'nickauthor': 'Missing Best Practice' }, 
            'body': 'An unimplemented best practice that is commonly accepted by the community. A missing best practice is not necessarily exploitable on its own, but combined with other weaknesses/vulnerabilities it could become an exploitable security vulnerability.' 
        },
        { 
            'author': { 'nickauthor': 'Privilege Escalation' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickauthor': 'Remote Code Execution' }, 
            'body': 'When user-controlled input, often code written in a specific programming language, is interpreted and executed on the remote server without proper filtering, escaping, or sandboxing.' 
        },
        { 
            'author': { 'nickauthor': 'Information Disclosure' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickauthor': 'SQL Injection' }, 
            'body': 'When user input can be embedded into SQL statements without proper filtering or quoting, leading to modification of query logic or execution of SQL commands' 
        },
        { 
            'author': { 'nickauthor': 'UI Redressing (Clickjacking)' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickauthor': 'Unvalidated / Open Redirect' }, 
            'body': 'Beautiful day in Portland!' 
        }
    ]
    return render_template("hacker.html",
        nickauthor = 'Home',
        user = user,
        posts = posts)


app.secret_key = 'development key'

if __name__ == '__main__':
  app.run(debug=True)
