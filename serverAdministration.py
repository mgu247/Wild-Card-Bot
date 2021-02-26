from command import Command

# Every module has to have a command list
commandList = []

# Example function:
# Just make sure that the function name in a command is the same
# Make sure every function is async and has both client, message as parameters, and that await is used when sending your response
commandList.append(Command("!example", "exampleFunction"))
async def exampleFunction(client, message):
    response = "This is an example of a function setup."
    await message.channel.send(response)

# Display a list of either all command functionality
commandList.append(Command("!help", "help"))
async def help(client, message):
    # This will display a response that will hold descriptions of all of the commands
    response = """`!help` : Displays a page of all commands and their descriptions.\n
`!commands` : This command will display all of the available comamnds\n
`!users` <optional_arg> : Will display a list of all users and their roles with no argument,
but when given a role it will display all users with the given role.\n"""
    await message.channel.send(response)


# Display a list of either all Users or only Users with a certain role
commandList.append(Command("!users", "displayAllUsers"))
async def displayAllUsers(client, message):
    # User List to hold all members in the server
    userList = message.guild.members
    response = ""
    if len(message.content.split(" ")) > 1:
        response = getUsersFromRole(userList, message.content.split(" ")[1])
    else:
        response = getAllUsers(userList)
    await message.channel.send(response)

# Get a string response with all users and their roles
def getAllUsers(userList):
    response = ""
    for user in userList:
        if user.display_name == "Wild Card Bot":
            continue
        response += "**" + user.display_name + "**\n__Roles:__ "
        for role in user.roles:
            response += role.name + " "
        response += "\n"
    return response
# Get a string response of a list of all users with a given role
def getUsersFromRole(userList, role):
    response = ""
    for user in userList:
        if user.display_name == "Wild Card Bot":
            continue
        for userRole in user.roles:
            if userRole.name == role:
                response += "**" + user.display_name + "**"
                response += "\n"
                break
    return response