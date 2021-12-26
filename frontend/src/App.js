import './index.css'
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import Projects from './pages/Projects';
import Team from './pages/Team';
import Time from './pages/Time';
import SideMenu from './components/Sidemenu';

function App() {
  return (
    
     <>
     <Router>
      <Navbar />
        <SideMenu />
        <Routes>
        <Route path='/' exact component={Home} />
          <Route path='/dashboard' component={<Dashboard />} />
          <Route path='/projects' component={<Projects />} />
          <Route path='/team' component={<Team />} />
          <Route path='/time' component={<Time />} />
          </Routes>
       <Footer />
     </Router>
    </>
    
    
  );
}

export default App;
