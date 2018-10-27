import openSocket from 'socket.io-client';
const socket = openSocket('http://172.16.84.241:8081');

function subscribeToStatusChange(cb) {
   socket.on('statusChange', status => cb(null, status));
 }

export { subscribeToStatusChange };
