package lyit.devops.oop2;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * This Class is responsible for file handling
 * @author Melissa Melaugh
 * Date Created: 16.09.2016
 * Date Modified: 16.06.2016
 *
 */
public class SomeFile {
	//Variables 
	private File file;
	private ArrayList<String> list;
	private ArrayList<String> addresses;
	private ArrayList<Integer> ports;
	private ArrayList<String> listeners;
	private ArrayList<String> deployed;
	
	/**
	 * Constructor
	 * @param aString	the filename to be parsed
	 */
	public SomeFile(String aString){
		this.list = new ArrayList<String>();
		this.file = new File(aString);
		this.addresses = new ArrayList<String>();
		this.ports = new ArrayList<Integer>();
		this.listeners = new ArrayList<String>();
		this.deployed = new ArrayList<String>();
	}
	
	/**
	 * This method parses the file
	 * @return	true if it was correctly parsed, false if unable to parse the file
	 */
	public boolean readFile(){
		try{
			//open the reader
		    BufferedReader reader = new BufferedReader(new FileReader(file));
		    String text = null;

		    //Read in the lines
		    while ((text = reader.readLine()) != null) {
		        this.list.add(text);
		    }
		    
		    //close the reader
		    reader.close();
		}catch(FileNotFoundException e){
			//Inform the reader of the error
		    System.out.println("The file you entered was not found.");
		    return false;
		}catch(IOException e){
			System.out.println("IOException");
		    return false;
		}catch(NullPointerException e){
			System.out.println("Null");
			return false;
		}
		fillLists();
		return true;
	}
	
	/**
	 * This method is responsible for filling the lists with the parsed information
	 */
	private void fillLists(){
		for(int i = 0; i < this.list.size(); i++){
			//Split up the string by spaces
			String[] str = this.list.get(i).split(" ");
			
			//Check each substring for wanted items
			for(int c=0; c<str.length; c++){
				String sub = str[c];
				
				if(sub.length() > 8 && (sub.substring(0, 5).equalsIgnoreCase("http:") || sub.substring(0, 5).equalsIgnoreCase("https:"))){
					//If it has http, add it to the address list
					this.addresses.add(sub);
				}else if(sub.equalsIgnoreCase("listener") && str.length >= 7 && c <= str.length - 4 && c - 1 >= 0){
					//If it contains a listener, add it to the listeners list
					this.listeners.add(str[c-1] + " " + sub + " " + str[c+1]);
					
					//Add the port to the ports list
					int len = str[c+4].length();
					String hold = (str[c+4].substring(len-4, len));
					try{
						int aNum = Integer.parseInt(hold);
						this.ports.add(aNum);
					}catch (Exception e){
						
					}
				}
				
				//If it contains something that was deployed add it to the deployed list along with how long it took.
				else if(sub.equalsIgnoreCase("deployed") && str.length >= 7 && c <= str.length - 3 && c - 3 >= 0){
					this.deployed.add(str[c-3] + " was deployed in " + str[c+2] + " " + str[c+3]);
				}
			}
		}
	}
	
	/**
	 * This method prints all of the network addresses saved to the addresses list
	 */
	public void printAddresses(){
		System.out.println();
		for(int i = 0; i <  this.addresses.size(); i++){
			System.out.println(this.addresses.get(i));
		}
		System.out.println();
	}
	
	/**
	 * This method prints all of the listeners saved to the listeners list
	 */
	public void printListeners(){
		System.out.println();
		for(int i = 0; i <  this.listeners.size(); i++){
			System.out.println(this.listeners.get(i));
		}
		System.out.println();
	}
	
	/**
	 * This method prints all of the ports saved to the ports list
	 */
	public void printPorts(){
		System.out.println();
		for(int i = 0; i <  this.ports.size(); i++){
			System.out.println(this.ports.get(i));
		}
		System.out.println();
	}
	
	/**
	 * This method prints all of the deployed applications saved to the deployed list
	 */
	public void printDeployed(){
		System.out.println();
		for(int i = 0; i <  this.deployed.size(); i++){
			System.out.println(this.deployed.get(i));
		}
		System.out.println();
	}
}
