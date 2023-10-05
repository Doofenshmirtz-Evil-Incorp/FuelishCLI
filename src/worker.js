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
      var uri=request.url.substring((request.url.toString()).lastIndexOf('.dev') + 5)
      return fetch(uri);
    },
  };
  