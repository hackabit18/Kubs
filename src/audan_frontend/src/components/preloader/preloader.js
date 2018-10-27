import React, {Component} from 'react';
import { subscribeToStatusChange } from '../../socket'
import { Redirect } from 'react-router'
import './preloader.css';

class PreLoader extends Component {
  constructor() {
    super()
    this.state = {
      prog: 0,
      redirectToDashboard: false,
      data: null,
    }

    subscribeToStatusChange((err, newval) => {
      console.log(newval)
      if(newval.progress) {
        this.setState({prog: newval.progress})
      }
      if (newval.data) {
         this.setState({redirectToDashboard: true, data: newval.data})
      }
    });
  }

  render() {
    if (this.state.redirectToDashboard) return (
      <Redirect
        to={{
          pathname: "/dashboard",
          state: { data: this.state.data }
        }}
      />
    )

    return (
      <div className="preloader">
        <div className="lds-ellipsis">
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </div>
        <div>Please wait while our minions analyze your video</div>
        <div>This may take a while</div>
        <div><h2>Processing...</h2></div>
        <div><h3>{Math.round(this.state.prog)}%</h3></div>
      </div>
    )
  }
}

export default PreLoader;
