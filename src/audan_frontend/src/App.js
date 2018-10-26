import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Header from './components/header/header';
import Footer from './components/footer/footer';
import Homepage from './pages/homepage/homepage';
import './App.css';

const App = () => {
  return (
    <BrowserRouter basename="/aclakg">
      <div className="App">
        <Header />
          <Switch>
            <Route exact path='/' component={Homepage}/>
          </Switch>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;