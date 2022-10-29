
OAUTH 2.0 Authorization Framework

Reference: https://www.rfc-editor.org/rfc/rfc6749#section-1.3.1



Oauth 2.0 is a frame work that allows 3rd party applications
to obtain limited access to an HTTP service for a multitude of reasons

Oauth 2.0 allows users to, in broad terms, allow users to log into
certain sites with information from other accounts, primarily Google, Yahoo,
etc etc.

At first, this can seem like a security risk, because if the user
is able to log in with credentials from another website, either that
website would be able to access information from the resource owner
unknowingly, there could be transfers of unwanted data, and could lead to
information leaks if a website is not secure enough.

Oauth 2's solution to this is to introduce an authorization layer
separating the role of the client from that of the resource owner.

Basically, if a 3rd party website was requesting to get some sort of data
on behalf of a client, they would be issued their own set of credentials,
seperate to the clients credentials, that would only be able to access
that one resource. This "set of credentials", also called an access token,
allows the client to transfer information they want to other services
and have them stay secure, without compromising any of their other data.
The actual process is has some more steps and is a little
more in depth then that, but layman's terms, that is what happens

     +--------+                               +---------------+
     |        |--(A)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+


The figure above shows in more detail how the client and
the resource server actually communicate.

One of the most important parts and the highlight of Oauth 2.0 is
the Authorization Code. It is used as the intermediary between the
client and the resource owner through the Authorization server.
The authorization server is what is used to authenticate the client,
validate authorization grants, and issue access tokens. In essence,
taking the security part away from the resource server and becoming
the "middle man" in the interaction.

Instead of requesting authorization directly from the resource owner,
the client directs the resource owner to an authorization sever, which
in turn, directs the resource owner back to the client with the
authorization code. This type of interaction allows the authentication
and transmission of the access token to not pass through
the resource owner's user-agent, which could expose it to unwanted
individuals, including the resource owner, and just allows for a more
secure system.


