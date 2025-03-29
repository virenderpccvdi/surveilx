# Base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the source files
COPY . .

# Build the app (if necessary)
RUN npm run build

# Expose the port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
