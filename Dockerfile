FROM node:12-alpine
WORKDIR /DevOps-users
COPY . .
RUN yarn install --production 
CMD ["node", "/app/src/index.js"]
