package lyit.devops.oop2;

import java.util.Scanner;

/**
 * This class is responsible for Display and running user choices
 * @author Melissa Melaugh
 * Date Created: 16.09.2016
 * Date last updated: 16.09.2016
 */
public class Run {
	static Scanner keyIn;
	
	/**
	 * This method offers the user choices on what to do with the program
	 */
	public void run(){
		//Setup
		SomeFile aFile = new SomeFile("C:/Users/SolarLunix/Desktop/ToRead.txt");
		keyIn = new Scanner(System.in);
		boolean running = true;
		boolean read = false;
		
		//Start program:
		System.out.println("Welcome to Melissa's file parsing system.");
		while(running){
			String options = "\nPlease enter an option number: "
					+ "\n\t1: Enter a file path "
					+ "\n\t2: Search for a file"
					+ "\n\t0: Exit";
			//Ask the user what they would like to do
			int choice = getNumResponse(options, 0, 2);
			
			if(choice == 1){
				//Enter a file path
				String file = getStrResponse("Enter the full file path:");
				aFile = new SomeFile(file);
				read = aFile.readFile();
			}else if(choice == 2){
				//Search for a file
				System.out.println("I'm sorry, but this feature has not been created.");
			}else{
				//Exit
				running = false;
			}
			
			while(read){
				options="\nPlease enter an option number:"
						+ "\n\t1: Print all servers and IP Addresses"
						+ "\n\t2: Print all listeners"
						+ "\n\t3: Print all ports"
						+ "\n\t4: Print all deployed applications"
						+ "\n\t0: Main Menu";
				choice = getNumResponse(options, 0,4);
				if(choice == 1){
					//Print Servers and IP Addresses
					aFile.printAddresses();
				}else if(choice == 2){
					//Print all Listeners
					aFile.printListeners();
				}else if(choice==3){
					//Print all Ports
					aFile.printPorts();
				}else if(choice==4){
					//print all deployed applications
					aFile.printDeployed();
				}else{
					read = false;
				}
			}
		}
	}
	
	/**
	 * This method prompts the user for a response, and returns the String they responded with
	 * @param aString	The prompt
	 * @return			The String value that the user entered
	 */
	static public String getStrResponse(String aString){
		String response = "";
		while(true){
			System.out.println(aString);
			response = keyIn.nextLine();
			if(!response.isEmpty()){
				break;
			}
		}
		return response;
	}
	
	/**
	 * This method prompts the user for an integer response and returns the value.
	 * @param aString	The prompt
	 * @param min		The minimum value the returned integer can be
	 * @param max		The maximum value the returned integer can be
	 * @return			The user's integer choice
	 */
	static public int getNumResponse(String aString, int min, int max){
		Boolean gotResponse = false;
		int response = min - 1; //Set response to a number that cannot change gotResponse to true
		do{
			//Print out the options in aString
			System.out.println(aString);
			if(keyIn.hasNextInt()){
				//Get the next int and store it as the response
				response = keyIn.nextInt();
				keyIn.nextLine();
				if(response >= min && response <= max){
					//If the response is within the parameters the loop can be exited
					gotResponse = true;
				}else{
					//If the response is outside of the parameters, inform the user and prompt again
					System.out.println("Option not valid");
				}
			}else{
				//Inform the user that there was an error with what they entered and prompt again
				keyIn.next(); //Ensures that there is not an infinite loop of prints
				System.out.println("You must enter a numeric value then press enter.");
			}
		}while(!gotResponse);
		return response;
	}
	
	/**
	 * This method shuts down the program
	 */
	public void shutdown() {
		System.out.println("Thank you for using the file parsing system");
		if (keyIn != null) {
			//Close the scanner
		    keyIn.close();
		}
	}
}
