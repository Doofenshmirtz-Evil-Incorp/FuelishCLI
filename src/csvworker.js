export default {
    async fetch(request) {
      async function MethodNotAllowed(request) {
        return new Response(`Method ${request.method} not allowed.`, {
          status: 405,
          headers: {
            Allow: "GET",
          },
        });
      }
      // Only GET requests work with this proxy.
      if (request.method !== "GET") return MethodNotAllowed(request);
      var resp=await fetch(request.url.substring((request.url.toString()).lastIndexOf('.dev') + 5));
      let response = new Response(resp.body, resp);
      response.headers.set("Access-Control-Allow-Origin","*");
      response.headers.append("Vary", "Origin");
      return response;
    },
  };
  