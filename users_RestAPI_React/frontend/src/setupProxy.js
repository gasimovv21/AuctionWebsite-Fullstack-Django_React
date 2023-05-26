const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
app.use(
    createProxyMiddleware('/api-users', {
      target: 'http://127.0.0.1:8000/api/', // API endpoint users
        changeOrigin: true,
        pathRewrite: {
        "^/api-users": "",
    },
    headers: {
        Connection: "keep-alive"
    }
    })
);
app.use(
    createProxyMiddleware('/api-items', {
      target: 'http://127.0.0.1:8001/api/', // API endpoint items
        changeOrigin: true,
        pathRewrite: {
        "^/api-items": "",
    },
    headers: {
        Connection: "keep-alive"
    }
    })
);
}