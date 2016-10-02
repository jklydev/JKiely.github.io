---
layout: post
---

So until recently my understanding of how OAuth2 works has been as follows:

1. Get the keys for the thing you want to oauth into.
2. Get the gem/package for oauthing into that particular thing.
3. Done.

However, recently I wanted to use the Recurse Center API for oauthing, which didn't have any of those convenient packages that I'm use to having do all of the work for me. I was working in Go, and so I still had the [Go OAuth2 package](https://github.com/golang/oauth2) to do *most* of the work for me, but it seemed that if I was going to dig into this at all I might as well learn how it actually works. So here is what I know about how OAuth2 works so far:

### Step 1: Register your application
Regardless of what packages you're using you still need the service to actually know about you, so go to wherever you need to go to register and get a Client ID and a Client Secret code. As you can probably guess from the names, the Client ID will be public knowledge, while the Client Secret will (should) be known only to you and the site you're authing with.

### Step 2: Redirect you user to the service Auth URL
So now you have an app, some other site knows about your app, and you have a user trying to log in via that other site, how do you get them authed? First you need to redirect them to the other sites Auth end point (maybe something like example.com/oauth/auth), you need to include two things as params with this redirect: Your Client ID, so they know who sent you, and the url you want the site to redirect you user back to after they give permission.

There are also three other parameters you can choose to specify or not: Firstly you can give a state string, is is typically a short string of random character that the authing site will return unmodified. The purpose of this is to protect against [Cross-Site Request Forgery](https://tools.ietf.org/html/rfc6749#section-10.12), and it can be a random value that you store per user session, a hash of the users information, or some other value tied to a given user. It ensures then when the client is redirected back to your site (step three) that the request actually originated from that user on your site, and not a third party who has tricked them into following a link (look [here](http://security.stackexchange.com/a/57886) for more information). Secondly you can set the scope, telling the service that you only want to access parts of this users account, for example checking their identity but not reading their email. Thirdly there is the response type. OK so this isn't actually optional but it is pretty much always set to code, some non-standard OAuth methods allow you to set this to token and get the token immediately without any of the following steps (But with some additional preceding ones, such as making a post request with the username and password).

So in the end your request will end up looking something like this: `site.com/oauth2/auth?client_id=foobar&redirect_uri=myapp.com/site_redirect&scope=public&state=SOMESHAHASH`

Once the user reaches this site, they can choose to log in and give you permission to access their data (or not).


### Step 3: Get the auth token from the token endpoint
Assuming the user gives you app permission to access their data, the site should then redirect them back to the url you provide, along with the authorization code and the state string you provided as parameters. As mentioned above, the first thing you should do is check the state string. If that checks out, then you need to grab the code from the params and make a request to the site's token url. This time the request goes directly from your server to the site's server, without the user doing anything. In the parameters of the request you should include both the code and your shared secret. If the code and the Client Secret both check out then the site should provide you with four things: Firstly the access token that you can use to do whatever the site has now authorized you to do, secondly the type of token they have granted you (usually just of type 'token'), thirdly the refresh token that you can use to generate a new access token if it expires, and finally how long until it expires (which can be set to zero in the case that it never expires).

### Summary
So if a users wants to OAuth into you app via another site, you have to send them to that site with some information on who you are and what you want to do. They then need to tell the site it's OK for you to access their data, and the site will send them back with a code confirming that you have their permission to access their data. Your app then takes that code and goes directly to the other site, where you confirm you are who you say you are and show them the code that confirms you're allowed to access what you say you're allowed to access. The site then give you a token that gives you permission to do whatever that is on behalf of the user.

There are still some parts I don't understand, for example what exactly to do with the refresh token. But all in all I think I have the gist of it. As part of this learning effort I build a wrapper around the RC API in Go, to make other lives easier in the future. You can see the code for that [here](https://github.com/JKiely/RC-API).



### Sources:
* [This](http://stackoverflow.com/a/32534239/3878507) Stack Overflow answer gave me the high level context to understand what was going on.
* [This](https://gist.github.com/mziwisky/10079157) give a bit more detail.
* The [Go OAuth2 Docs](https://godoc.org/golang.org/x/oauth2) and reading [the code itself](https://github.com/golang/oauth2) helped me understand what was happening on a technical level.
* Where I still didn't get it I looked at the [official spec](https://tools.ietf.org/html/rfc6749), which is surprisingly readable!
