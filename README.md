#  Automated Vending Coffee Machine Simulator

Welcome to the **Coffee Machine Simulator**! This is a clean, interactive command-line application built in Python that brings a real-world coffee vending machine to your terminal. 

Whether you want to order a hot cup of Mocha as a customer or check inventory levels as a technician, this program handles it all seamlessly!

---

##  Key Features

The application is strictly split into two modules to mirror a real-life vending machine:

###  Customer Experience
* **Interactive Menu:** Lists popular drinks like Espresso, Latte, Cappuccino, Mocha, and Flat White alongside their prices.
* **Smart Resource Validation:** The machine checks if it has enough exact ingredients (water, milk, coffee, chocolate) *before* taking your money.
* **Strict Payment Gateways:** * Calculates and returns precise cash change if you overpay.
  * Grants up to **3 attempts** to correct underpayments before canceling the order.

###  Secure Admin Portal
* **Password-Protected Interface:** Accessible by typing a secret key (`admin`) at the drink prompt.
* **Live Audit Reports:** Monitors remaining ingredient quantities (in ml and grams) and tracks total profit accumulated.
* **Restocking Utilities:** Allows operators to cleanly refill depleted raw materials back into the system without restarting the code.
* **Safe Shutdown:** Offers a controlled operational kill-switch to turn off the machine completely.

---

##  Built With

* **Python 3.x** — Core logical structures, dictionary mapping, data validation, and state control loops.
* **Virtual Environments (venv)** — Used to isolate dependencies and maintain code reliability.

---

##  How to Setup and Run

Getting the machine up and running on your local computer is incredibly straightforward:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Izazaqsa/Coffee-Machine-Simulator.git](https://github.com/Izazaqsa/Coffee-Machine-Simulator.git)
