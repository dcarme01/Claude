# 📱 Deploy Kalshi Analyzer from Your iPhone

This guide shows you how to deploy the Kalshi Bet Analyzer entirely from your iPhone - no computer needed!

## 🚀 Quick Deploy (Recommended: Render.com)

Render offers a free tier and is the easiest to deploy from mobile.

### Step-by-Step Instructions

#### 1. Fork the Repository on GitHub

1. Open Safari on your iPhone
2. Go to your repository: `https://github.com/dcarme01/Claude`
3. Tap the "Fork" button (top right, may need to tap "Request Desktop Site" in Safari settings)
4. Confirm to create your fork

#### 2. Sign Up for Render

1. Visit: **https://render.com**
2. Tap "Get Started" or "Sign Up"
3. Sign up with your GitHub account (easiest option)
4. Authorize Render to access your GitHub repositories

#### 3. Deploy Your App

1. Once logged into Render, tap **"New +"** (top right)
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - If not already connected, tap "Configure account"
   - Grant access to your forked repository
4. Find your repository in the list and tap **"Connect"**
5. Configure the deployment:
   - **Name**: `kalshi-analyzer` (or any name you like)
   - **Region**: Choose closest to you
   - **Branch**: `claude/kalshi-bet-analyzer-01BuS24gifahD8e3wcv28RtQ`
   - **Root Directory**: `kalshi-analyzer`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Scroll down to **Environment Variables** section
7. Add your Kalshi credentials:
   - Tap **"Add Environment Variable"**
   - Key: `KALSHI_EMAIL`
   - Value: `your@email.com`
   - Tap **"Add Environment Variable"** again
   - Key: `KALSHI_PASSWORD`
   - Value: `your_password`
   - Tap **"Add Environment Variable"** again
   - Key: `KALSHI_DEMO_MODE`
   - Value: `true` (for safe testing)
8. Scroll to bottom and tap **"Create Web Service"**

#### 4. Wait for Deployment

- Render will build and deploy your app (takes 2-5 minutes)
- You'll see build logs in real-time
- When done, you'll see "Live" status with a green dot

#### 5. Access Your App

1. Look for your app URL at the top (looks like: `https://kalshi-analyzer-xxxx.onrender.com`)
2. Tap the URL to open your app
3. Bookmark it or add to home screen!

### 📌 Add to Home Screen

1. In Safari, tap the Share button
2. Scroll down and tap "Add to Home Screen"
3. Name it "Kalshi Analyzer"
4. Tap "Add"
5. Now you have a native-looking app icon!

---

## 🔄 Alternative: Railway.app

Railway is another great free option:

1. Visit: **https://railway.app**
2. Sign up with GitHub
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your forked repository
6. Railway will auto-detect settings
7. Add environment variables in the "Variables" tab:
   - `KALSHI_EMAIL`
   - `KALSHI_PASSWORD`
   - `KALSHI_DEMO_MODE=true`
8. Your app will auto-deploy!
9. Go to "Settings" → "Networking" → "Generate Domain" to get your URL

---

## 🔄 Alternative: Replit (Easiest but May Cost)

Replit lets you run Python apps directly from your phone:

1. Visit: **https://replit.com** in Safari
2. Sign up with GitHub
3. Tap **"Create Repl"**
4. Select **"Import from GitHub"**
5. Paste your repository URL
6. Once imported, add a `.env` file with:
   ```
   KALSHI_EMAIL=your@email.com
   KALSHI_PASSWORD=your_password
   KALSHI_DEMO_MODE=true
   ```
7. Tap the "Run" button
8. Your app will open in a built-in browser

---

## ⚙️ Managing Your Deployment

### Update Environment Variables

**On Render:**
1. Go to your service dashboard
2. Tap "Environment"
3. Edit variables as needed
4. Changes apply immediately

**On Railway:**
1. Open your project
2. Tap "Variables"
3. Edit or add variables
4. Redeploy if needed

### Switch to Production Mode

When you're ready to use real money (not demo mode):
1. Go to environment variables
2. Change `KALSHI_DEMO_MODE` from `true` to `false`
3. Save and redeploy

### View Logs

**On Render:**
- Tap "Logs" tab to see app activity

**On Railway:**
- Tap "Deployments" → Latest deployment → "Logs"

---

## 🆓 Free Tier Limitations

### Render Free Tier:
- ✅ 750 hours/month (plenty for personal use)
- ⚠️ Spins down after 15 min inactivity (cold start ~30 sec)
- ✅ Perfect for this app

### Railway Free Tier:
- ✅ $5 credit per month
- ✅ Should cover light usage
- ⚠️ Need to add payment method after trial

### Tips for Free Tier:
- Use demo mode to avoid API rate limits
- Access regularly to keep instance warm
- Consider upgrading if you use it daily

---

## 🔒 Security Notes

- ✅ Environment variables are encrypted
- ✅ Your credentials never appear in code
- ⚠️ Use demo mode until you're comfortable
- 🔐 Never share your app URL publicly (contains your creds)

---

## 🎉 You're Done!

Your Kalshi Analyzer is now:
- ✅ Running in the cloud
- ✅ Accessible from anywhere
- ✅ Available 24/7
- ✅ No computer needed!

Just open your app URL on your iPhone and start analyzing markets! 📊

---

## 💡 Tips

1. **Bookmark the URL** in Safari for quick access
2. **Add to Home Screen** for app-like experience
3. **Enable notifications** in Safari settings for updates
4. **Share with friends** (but don't share if you added real credentials!)

## ❓ Troubleshooting

**App won't load?**
- Wait 30 seconds (free tier cold starts)
- Check environment variables are set correctly
- View logs for error messages

**"Not configured" error?**
- Make sure `KALSHI_EMAIL` and `KALSHI_PASSWORD` are set in environment variables

**Build failed?**
- Check that the branch name is correct
- Ensure root directory is set to `kalshi-analyzer`
- View build logs for specific errors

---

Need help? Check the logs in your deployment dashboard or open an issue on GitHub!
