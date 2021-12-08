import './index.css'
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import SideMenu from './components/SideMenu';

function App() {
  return (
    <main>
      <Navbar />
      <div className="min-h-screen flex flex-row">
        <SideMenu />
        <h1 className="text-2xl">PRO[J]TOR APP HOME PAGE</h1>
      </div>
      <Footer />
    </main>
  );
}

export default App;
