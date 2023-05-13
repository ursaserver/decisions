We could visualize two different pictures for rate limiting. Consider the followings written using pseudo-code:

```
#
# Picture 1
#

let ursa be Ursa instance
let upstream be an Upstream server
let client be a Downstream host 

while True {
    ursa.recv_request(handle_request)
} 

fn handle_request(req, res){
    if should_accept(req){
        get_upstream_response(req).then(
            (res) => res.wite(res)
        )
    }else{
        // Do something to handle rejection
    }
}

```


```
#
# Picture 2
#

let ursa be Ursa instance
let upstream be an Upstream server
let client be a Downstream host 

while True {
    ursa.recv_request(handle_request)
} 

fn handle_request(req, res){
    if should_accept(req){
        send_request_upstream(req)
    }else{
        // Do something to handle rejection
    }
}

```

For requests that are filtered-in, the picture 1 proposes a mode where Ursa
fetches response from upstream and sends that response downstream. Ursa is responsible for receiving requests from downstream, gathering the appropriate response for the request (by asking upstream) and writing the response downstream.

However, in the case of picture 2, Ursa is only responsible for forwarding appropriate (filtered-in) requests upstream. The upstream then has the responsibility of sending response to the client (downstream). 

While picture 2 looks good in that it's following the philosophy of separation of concern, there are other problems that it sweeps under the rug. Should Ursa drop connection to downstream once it receives the request? If so, won't the client get some sort of bad response? In the case of websocket connections, it might not be a problem since Ursa could close the connection immediately after getting the request and Upstream could initiate a new downstream connection if need be. However it looks problematic in the case of HTTP connections.

Therefore, we'll implement picture 1.


## Conclusion
1. Ursa receives request
1. If rate limited, rejects. Terminates the connection.
1. **Else**, 
1. Generates appropriate response for the the request by requesting upstream.
1. Writes the generated response downstream. Terminates the connection.
