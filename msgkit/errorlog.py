class ErrorLog:

    def __init__(self):
        self.causenum = 0

    def printerror(self, num, msg):
        '''
        Prints the error number, message received, and potential causes and solutions if desired.
        The causes are printed out in decreasing order of likelihood.
        '''
        print(f'\nError received: {num}\n')
        print(f'Response from server: {msg}\n')
        print('Possible causes:')

        if str(num) == '404':
            causes = [
                'The URL was written incorrectly or typed into the browser incorrectly',
                'The resource was moved, deleted, or is expired',
                'The file may be in a different path/the path is typed in incorrectly',
                'The server may not have the necessary permissions to access the requested resource',
                'Misconfigured server settings, such as incorrect routing rules or missing configuration files',
                'If a web server is not configured to serve a default page (e.g., "index.html") and you don\'t specify a specific page in the URL',
                'Websites using content management systems (CMS) may generate 404 errors if the requested URL corresponds to a non-existent or unpublished page',
                'The website may be using URL rewriting to create user-friendly URLs (e.g., from /page?id=123 to /page/123)',
                'When working with APIs, there could be changes in the API\'s structure, endpoint names, or versioning',
                'Problems with DNS (Domain Name System) configuration',
                'In a network with load balancers or reverse proxies, misconfiguration can cause requests to be routed to non-existent endpoints',
            ]
            self.printCauses(causes)
            print('\nPossible solutions:')
            solutions = [
                'Check the URL or path',
                'Verify the resource exists',
                'Check the server logs',
                'Check permissions for the file or directory',
                'Check if cache and content management systems are interfering',
            ]
            self.printSolutions(solutions)
        elif str(num) == '403':
            causes = [
                'The client lacks the necessary permissions to access this source (lack of authentification, not having appropriate credentials, an access control list that prohibits access, etc)',
                'If the credentials provided for authentification or incorrect or nonexistent'
                'Your IP may be prohibited from accessing the source (blacklisted) or has not been granted access (whitelisted)'
                'You may have directory listing disabled, meaning you will not be able to view contents of the directory',
                'You may not possess permissions to access a file on the requested source',
                'A firewall, Web Application Firewall (WAF) or another web application security device may have blocked your request to access the source',
                'The client may have exceeded the amount of requests alotted to it by the website or API',
                'Source may have restrictions on what methods of HTML can be used',
                'The website may be using a specific Referer in its header that may be missing or incorrect in the request, triggering a 403 error',
                'There may be a misconfiguration of the web server or its security settings, which could lead to a 403 error',
            ]
            self.printCauses(causes)
            print('\nPossible solutions:')
            solutions = [
                'Check permissions for the website and/or its resources',
                'Be sure to ensure proper authentification',
                'Address the application\'s or server\'s security measures (e.g. Disable VPN/Hotspot, make fewer requests to access the source, etc.)',
                'Enable directory listing',
            ]
            self.printSolutions(solutions)

    def printCauses(self, causes):
        if self.causenum != 0:
            causes = causes[:self.causenum]
        for i, cause in enumerate(causes):
            print(f'{i + 1}.', cause)

    def printSolutions(self, solutions):
        for i, solution in enumerate(solutions):
            print(f'{i + 1}.', solution)