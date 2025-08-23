## Access the Admin Console:

Open your web browser and navigate to the Payara Server Admin Console. Typically, this is accessed via http://localhost:4848 unless you've changed the default port or are accessing a remote server.
Login:

If prompted, enter your administrative credentials to log in.

## Navigate to JVM Options:

In the left-hand navigation pane, expand the Configurations section.
Click on server-config (or the configuration you're working with if you have multiple).
Now, under the Java VM category, click on JVM Options.

## Locate Existing Heap Memory Settings:

In the JVM Options list, look for options that start with -Xms (initial heap size) and -Xmx (maximum heap size). These options might look something like -Xms512m and -Xmx1024m, where 512m and 1024m represent the memory sizes in megabytes.

## Modify Heap Memory Settings:

Click on the option you want to modify (either -Xms or -Xmx).
In the edit box, adjust the value to your desired memory size. For example, to set the maximum heap size to 2 gigabytes, you would change -Xmx1024m to -Xmx2048m.
Click Save to apply the changes.

## Restart Payara Server:

For the changes to take effect, you'll need to restart the Payara Server. You can do this from the Admin Console by navigating to the Server tab and clicking Restart.

## Verify Changes:

After the server restarts, revisit the JVM Options to ensure your changes have been saved and applied correctly.
Please note: Adjusting heap memory settings can impact the performance and stability of your applications and the server. Always monitor the server after making such changes and ensure you have backups of any critical data.


[Back to Troubleshooting](https://github.com/hmislk/hmis/wiki/Troubleshooting)



[Back](https://github.com/hmislk/hmis/wiki)
