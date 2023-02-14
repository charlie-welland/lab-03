# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- team member 1
Charlie Welland
- team member 2
Charlotte Kroll
## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

RESTful APIs are scalable because they dont store any client context. 
This means that all the information of the client will be sent in each request.
Because none of the servers store the client context, it allows for the ability to 
seamlessly create new servers to manage the increased load of requests.

Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?

The mail server is providing json objects to the user. These objects contain information
on who the sender is, who the reciever is, and the contents of the email. 

Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?

The PUT method is not being used in our mail server. One way to implement this REST
Method would be to use it in an email editing portion of the email where if a 
user were to accidentally have a typo in their email, they could fix it in a certain
amount of time after they have sent the message.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!

API keys can be used as a method of tracking activity or preventing unauthorized access 
to some sort of data. Some sort of data file could only be allowed to be accessed by a 
certain API key and therefore could keep classified data classified.

I used ChatGPT for information on this topic.
