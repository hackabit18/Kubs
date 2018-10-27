import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom'
// import Header from './components/header/header';
import Footer from './components/footer/footer';
import Homepage from './pages/homepage/homepage';
import Dashboard from './pages/dashboard/dashboard';
import './App.css';

const App = () => {
  return (
    <BrowserRouter>
      <div className="App">
          <Switch>
            <Route exact path='/' component={Homepage}/>
            <Route exact path='/dashboard' component={Dashboard}/>
            {/* // Add How it works */}
          </Switch>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
