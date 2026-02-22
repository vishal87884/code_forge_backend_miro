# 1. Use the version of Node you already have installed (v24)
FROM node:24-slim

# 2. Create the app directory inside the container
WORKDIR /app

# 3. Copy package files first (this makes builds faster)
COPY package*.json ./

# 4. Install dependencies
RUN npm install --production

# 5. Copy your index.js and other files
COPY . .

# 6. Command to start your worker
CMD ["node", "index.js"]
