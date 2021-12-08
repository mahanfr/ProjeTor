import '../index.css'

function Navbar() {
  return (
    <header>
      <nav>
        <div className="flex flex-row justify-between items-center w-full bg-gray-900 py-3 px-5">
          <div id="navbar-right" className="flex flex-row items-center">
            <div className="mr-5 flex flex-row items-center space-x-2">
              <svg class="w-5 h-5 text-blue-500 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.82 403.82">
                <g id="Layer_2" data-name="Layer 2">
                  <g id="Icon">
                    <circle class="cls-1" cx="92.67" cy="92.67" r="92.67" />
                    <circle class="cls-1" cx="92.67" cy="310.91" r="92.67" />
                    <circle class="cls-1" cx="310.91" cy="92.67" r="92.67" />
                    <path class="cls-1" d="M403.82,311.15a92.67,92.67,0,0,1-185.34,0" />
                  </g>
                </g>
              </svg>
              <a className="text-2xl font-mono font-bold text-gray-200" href="{% url 'index' %}">Pro[j]tor</a>
            </div>
            <ul className="hidden md:flex md:flex-row space-x-4 text-gray-300 font-mono">
              <li>
                <a href="{% url 'index' %}">Home</a>
              </li>
              <li>
                <a href="{% url 'pricing' %}">Pricing</a>
              </li>
              <li>
                <a href="{% url 'support' %}">Support</a>
              </li>
              <li>
                <a href="{% url 'about' %}">About</a>
              </li>
            </ul>
          </div>
          <div className="flex flex-row space-x-3 items-center" id="navbar-left">
            <a href="#" className="text-white"></a>
            <span className="relative">
              <span className=""><a className="mx-1 px-1 text-white" href="#"><i className="fas fa-bell"></i></a></span>
              <span className="absolute top-0 right-0 bg-red-800 rounded-full w-2 h-2" style={{ z_index: 10 }}></span>
            </span>
            <a href="#" className="text-white "><i className="fa fa-gear"></i></a>
            <a href="{% url 'logout' %}" className="text-white "><i className="fa fa-sign-out-alt"></i></a>
            <button id="navbar-button" className="block md:hidden"><i className="text-xl text-white fas fa-bars"></i></button>
          </div>
        </div>
        <div id="navbar-hidden-menu" className="hidden md:hidden bg-gray-800 w-full pb-2 px-5">
          <ul className="text-center text-white">
            <li className="py-1"><a href="{% url 'index' %}">Home</a></li>
            <li className="py-1"><a href="{% url 'pricing' %}">Pricing</a></li>
            <li className="py-1"><a href="{% url 'support' %}">Support</a></li>
            <li className="py-1"><a href="{% url 'about' %}">About</a></li>
          </ul>
        </div>
      </nav>
    </header>
  );
}

export default Navbar;
