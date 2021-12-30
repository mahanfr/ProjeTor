import './index.css'
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import SideMenu from './components/SideMenu';

function App() {
  return (
    <main>
      <Navbar />
      <div className="min-h-screen flex flex-row">
        <div className="bg-gray-600 h-screen w-44">
          <p className="text-gray-100 text-lg ml-2 my-3">Projects:</p>
          <ul>
            <li className="bg-gray-500 hover:bg-gray-700 ">
              <div className="flex flex-row items-center py-1">
                <i className="fa fa-circle text-white ml-1"></i>
                <p className="text-white text-xl ml-2">First</p>
              </div>
            </li>
            <li className="hover:bg-gray-700 ">
              <div className="flex flex-row items-center py-1">
                <i className="fa fa-circle text-white ml-1"></i>
                <p className="text-white  text-xl ml-2">Second</p>
              </div>
            </li>
            <li className=" hover:bg-gray-700 ">
              <div className="flex flex-row items-center py-1">
                <i className="fa fa-circle text-white ml-1"></i>
                <p className="text-white text-xl ml-2">Third</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <Footer />
    </main>
  );
}

export default App;
