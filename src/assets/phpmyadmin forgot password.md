Screenshot_20250925_021242

The `ALTER USER` command you tried to use is not supported in the version of MariaDB that you are running. The syntax for changing a user's password in older versions of MariaDB (before 10.4) and MySQL is different.

-----

### **How to Fix the Syntax Error**

Instead of `ALTER USER`, you should use the `UPDATE` statement on the `mysql.user` table.

1.  Log in to the MariaDB shell as the root user with `sudo`:

    ```bash
    sudo mysql
    ```

2.  Run the following commands to change the password and reload privileges. **Replace `'janak0ff'` with your desired new password.**

    ```sql
    USE mysql;
    UPDATE user SET authentication_string = PASSWORD('janak0ff') WHERE User = 'root';
    UPDATE user SET plugin = 'mysql_native_password' WHERE User = 'root';
    FLUSH PRIVILEGES;
    ```

      - `USE mysql;` selects the `mysql` database, which contains user account information.
      - The first `UPDATE` statement sets the new password for the `root` user.
      - The second `UPDATE` statement ensures the correct authentication plugin is used for password-based login.
      - `FLUSH PRIVILEGES;` reloads the user privileges so the changes take effect immediately.

3.  Exit the MariaDB shell:

    ```bash
    exit
    ```

4.  You can now log in with the new password:

    ```bash
    mysql -u root -p
    ```

    Enter `janak0ff` (or your chosen password) when prompted.

**Important Note:** The `PASSWORD()` function is deprecated in newer versions of MySQL and MariaDB. However, for the version you are using (MariaDB 10.1), this is the correct and functional method.



---

Here are the commands to create a new user named 'janak' with the password 'janak0ff' and grant them full privileges in MariaDB.

-----

### **Create a New User and Grant Privileges**

1.  First, log in to the MariaDB shell as the root user. Since your system uses the `auth_socket` plugin for the root user, you must use `sudo` to log in without a password:

    ```bash
    sudo mysql
    ```

2.  Once you're in the MariaDB shell, run the following commands to create the user, set their password, and grant them all privileges on all databases.

    ```sql
    CREATE USER 'janak'@'localhost' IDENTIFIED BY 'janak0ff';
    GRANT ALL PRIVILEGES ON *.* TO 'janak'@'localhost' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    ```

      - `CREATE USER 'janak'@'localhost' IDENTIFIED BY 'janak0ff';` creates a new user named **janak** who can connect from the local machine (`localhost`) and sets their password to **janak0ff**.
      - `GRANT ALL PRIVILEGES ON *.* TO 'janak'@'localhost' WITH GRANT OPTION;` gives the new user complete control (`ALL PRIVILEGES`) over all databases (`*.*`). The `WITH GRANT OPTION` allows this user to grant privileges to other users as well.
      - `FLUSH PRIVILEGES;` reloads the privilege tables, making the changes effective immediately.

3.  After running these commands, exit the shell:

    ```sql
    exit
    ```

You can now log in using the new user account and password:

```bash
mysql -u janak -p
```

Enter `janak0ff` when prompted for the password.