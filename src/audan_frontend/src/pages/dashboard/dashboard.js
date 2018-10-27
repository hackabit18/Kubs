import React, {Component} from 'react';
import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink, Jumbotron } from 'reactstrap';
import Plots from '../../components/plots/plots'
import './dashboard.css';

export default class Dashboard extends Component {

  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false,
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }

  render() {
    return (
      <div>
        <div className='header-dashboard'>
          <Navbar color="faded" light toggleable>
            <NavbarToggler right="true" onClick={this.toggle} />
            <NavbarBrand href="/">
              <p>AudAn</p>
            </NavbarBrand>
            <Collapse isOpen={this.state.isOpen} navbar>
              <Nav className="p-2" navbar>
                <NavItem>
                  <NavLink href="/">Home</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/team">The Team</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/contact">Contact Us</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/about">About Us</NavLink>
                </NavItem>
              </Nav>
            </Collapse>
          </Navbar>
        </div>
        <Jumbotron className="jumbodash">
          <h1 className="display-5">Your Report is Available</h1>
          <p className="lead">
            Below is a detailed analysis about the reactions and emotions of
            your audience during your speech
           </p>
        </Jumbotron>
        {this.props.location.state ?
          <Plots data={this.props.location.state.data}/>
        :
          <p style={{textAlign: 'center', padding: '10px'}}>Uh Oh! Try again from the homepage</p>
        }

      </div>
    );
  }
}
