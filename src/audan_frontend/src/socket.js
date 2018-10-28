import openSocket from 'socket.io-client';
const socket = openSocket('http://10.42.0.231:8081');

function subscribeToStatusChange(cb) {
   socket.on('statusChange', status => cb(null, status));
 }

export { subscribeToStatusChange };
