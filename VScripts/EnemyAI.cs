using UnityEngine;
using System.Collections;


public class EnemyAI : MonoBehaviour
{
    NavMeshAgent agent;
    public Transform target;
	public static Vector3 targetPosition;
	// AI movespeed on beeline mode, regular movespeed = 3.5 (nav mesh agent speed)
    public float moveSpeed = 1.5f;
    public static bool initialHit = false;
    public static bool enemyHit = false;
	[SerializeField]private float wanderDist = 100;
    //--- AI states ---//
	[SerializeField]private bool wander = true; // default state
	[SerializeField]private bool chase = false; // underlying state, if all other states are false will chase, as the nav mesh agent takes over
	[SerializeField]private bool scared = false; // hurt state
	[SerializeField]private bool manualMovement = false; // dumb, beeline state
	//-----------------//
	public float health = 100;
    [SerializeField]private float stamina = 100;
    private bool sight = false;
	private float rotationSpeed = 1.5f;
    private float hitCooldown = 0;
    private float hitCountdown = 1.5f;
	private float runBoredomCounter = 7;
	private float currentRunBoredom = 0;
    private float sightTimer = 0;
    private float sightMinimum = 2;

    // Use this for initialization
    void Start()
    {
        // setting up handle to refer to nav mesh agent, or smart AI component
        agent = GetComponent<NavMeshAgent>();
    }

    // Update is called once per frame
    void Update()
    {
        hitCooldown += Time.deltaTime;
        agent.SetDestination(targetPosition);

        // raycast to detect for player to hit
        RaycastHit hit;
        Ray ray = new Ray(transform.position, transform.forward);
        Ray ray2 = new Ray(transform.position / 1.5f, transform.forward);
        Ray ray3 = new Ray(transform.position / 2.5f, transform.forward);
        if (Physics.Raycast(ray, out hit, 1f))
        {
            if (hit.collider.tag == "Player")
            {
                if (hitCooldown > hitCountdown)
                {
                    PlayerHealth.health -= 20;
                    hitCooldown = 0;
                }
            }
        }

        // new raycast to simulate line of sight
        if (Physics.Raycast(ray, out hit, 30) || Physics.Raycast(ray2, out hit, 30) || Physics.Raycast(ray3, out hit, 30))
        {
            Debug.Log(sightTimer);
            Debug.DrawLine(transform.position, hit.point, Color.green);
            if (hit.collider.tag == "Player")
            {
                sight = true;
            }

        }   

        if (sight == true)
        {
            chase = true;
            wander = false;
        }
        else
        {
            chase = false;
            wander = true;
        }

        if (stamina <= 0)
        {
            chase = false;
            wander = true;
        }

        // default state is wander, only changes if raycast detects player
        if (wander == true)
		{
			Vector3 newPos = RandomNavSphere(transform.position, wanderDist, -1)/ 6;
			agent.SetDestination(newPos);
            agent.speed = 3;
            if (stamina <= 100)
            {
                stamina += Time.deltaTime * 6;
            }
        }

        //  second state, chase, disabling wander and taking on regular AI patterns
		if (chase == true) {
			stamina -= Time.deltaTime * 5;
			if (stamina <= 10) {
				chase = false;
				wander = true;
			}
		} else {
			stamina += Time.deltaTime * 2;
		}

        if (wander == false &&  scared == false)
        {
            chase = true;
        }

		// third state, scared, runs away from player
		if (scared == true) 
		{
			Vector3 moveDirection = transform.position - target.transform.position;
			agent.SetDestination (moveDirection);
			currentRunBoredom += Time.deltaTime;
			agent.speed = 4;
			chase = false;

			if (currentRunBoredom >= runBoredomCounter)
			{
				scared = false;
				wander = true;
			}
		}

		// fourth state, moves straight to player position, ignoring obstacles
		if (manualMovement == true && target != null)
		{
			// turns off smart ai and begins a process to slowly crawl over debris, switches off once off debris
			transform.position += (target.position - transform.position).normalized * moveSpeed * Time.deltaTime;
			transform.rotation = Quaternion.Slerp(transform.rotation, Quaternion.LookRotation(target.position - transform.position), rotationSpeed * Time.deltaTime);
		}

		// switches to scared state when hurt badly
		if (health <= 40 && currentRunBoredom <= runBoredomCounter) 
		{
			scared = true;
		}	

		// dead
		if (health <= 0)
		{
			Destroy(this.gameObject);
		}

    }
		
    // wandering calculations
    public static Vector3 RandomNavSphere(Vector3 origin, float dist, int layermask)
    {
        Vector3 randDirection = Random.insideUnitSphere * dist;
        randDirection += origin;
        NavMeshHit navHit;
        NavMesh.SamplePosition(randDirection, out navHit, dist, layermask);
        return navHit.position;
    }
		
    void OnCollisionEnter(Collision col)
    {
        // put enemy hit in collision function to maintain individual health variable in each enemy 
        if (initialHit == true)
        {
			// damages first target 
			health -= 20;
			initialHit = false;
			chase = true;
			wander = false;
			scared = false;
		}

		if (col.gameObject.tag == "Debris" && woodDebris.settled == true && scared == false)
        {
            // turns off smart AI and turns on dumb beeline enemies that can get through the rubble
            wander = false;
            manualMovement = true;
            gameObject.GetComponent<NavMeshAgent>().enabled = false;
        }
        // prevents flying debris right after destruction from glitching the AI
        else if (col.gameObject.tag == "Debris" && woodDebris.settled == false)
        {
            gameObject.GetComponent<NavMeshAgent>().enabled = false;
        }
        else
        {
            // once off debris, turns smart AI back on to find path of least resistance
            manualMovement = false;
            gameObject.GetComponent<NavMeshAgent>().enabled = true;
        }
    }
}
